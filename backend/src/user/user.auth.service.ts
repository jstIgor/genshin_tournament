import {
  BadGatewayException,
  BadRequestException,
  ForbiddenException,
  HttpException,
  Injectable,
  InternalServerErrorException,
  NotFoundException,
} from '@nestjs/common';
import { UserRepository } from './user.repository';
import { registerUserDto } from './dtos/register-user.dto';
import * as jwt from 'jsonwebtoken';
import { ConfigService } from '@nestjs/config';
import { User } from '@prisma/client';
import { loginUserDto } from './dtos/login-user.dto';
import * as argon from 'argon2';
import { Exclude, Expose, plainToInstance } from 'class-transformer';
import { UserAndToken } from './interfaces/user-token.interface';

@Exclude()
export class tokenPayload {
  @Expose()
  id: string;
  @Expose()
  role: string;
}
@Injectable()
export class UserAuthService {
  constructor(
    private userService: UserRepository,
    private configService: ConfigService,
  ) {}
  private readonly secret_key =
    this.configService.getOrThrow<string>('JWT_SECRET');

  private validateToken(token): tokenPayload {
    try {
      const tokenPl = jwt.verify(token, this.secret_key, {
        ignoreExpiration: true,
      });
      return plainToInstance(tokenPayload, tokenPl);
    } catch (error) {
      throw new BadRequestException('токен не валидный');
    }
  }
  private generateToken(payload: tokenPayload): string {
    return jwt.sign({ id: payload.id, role: payload.role }, this.secret_key, {
      expiresIn: '5d',
    });
  }

  async login(dto: loginUserDto): Promise<UserAndToken> {
    const userFromDb = await this.userService.findUserByName(dto.name);
    if (!userFromDb) {
      throw new NotFoundException('Пользователь с таким никнеймом не найден !');
    }
    const isPasswordValid = await argon.verify(
      userFromDb.passwordHash,
      dto.password,
    );
    if (!isPasswordValid) {
      throw new ForbiddenException('Пароль неверный');
    }
    const payload = plainToInstance(tokenPayload, userFromDb);
    const token = this.generateToken(payload);
    return { user: userFromDb, token: token };
  }

  async checkout(token): Promise<UserAndToken> {
    const data = await this.validateToken(token);
    const userCandidate = await this.userService.findUserById(data.id);
    if (!userCandidate) {
      throw new BadRequestException('не валидный токен');
    }
    const payload = plainToInstance(tokenPayload, userCandidate);
    const newToken = this.generateToken(payload);
    return { user: userCandidate, token: newToken };
  }

  async register(dto: registerUserDto): Promise<UserAndToken> {
    const userCandidate = await this.userService.findUserByName(dto.name);
    if (userCandidate) {
      throw new BadGatewayException(
        'User with this nickmname already exists !',
      );
    }
    const user = await this.userService.createUser(dto);
    if (!user) {
      throw new InternalServerErrorException('failed when creating a user');
    }
    const payload = plainToInstance(tokenPayload, user);
    const jwtToken = this.generateToken(payload);

    return { user: user, token: jwtToken };
  }
}
