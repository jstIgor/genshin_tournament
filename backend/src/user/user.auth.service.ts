import { BadGatewayException, HttpException, Injectable, InternalServerErrorException } from '@nestjs/common';
import { UserService } from './user.service';
import { registerUserDto } from './dtos/register-user.dto';
import * as jwt from 'jsonwebtoken';
import { ConfigService } from '@nestjs/config';
import { User } from '@prisma/client';
@Injectable()
export class UserAuthService {
  constructor(private userService: UserService) {}

  async register(dto: registerUserDto) {
    console.log(dto);
    const userCandidate = await this.userService.findUserByNickName(
      dto.nickName,
    );
    if (userCandidate) {
      throw new BadGatewayException(
        'User with this nickmname already exists !',
      );
    }
    const user = await this.userService.createUser(dto);
    if(!user){
      throw new InternalServerErrorException("failed when creating a user")
    }
    const jwtToken = jwt.sign(
      { id: user.id, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: '5d' },
    );

    return {
      user,
      jwtToken,
    };
  }
}
