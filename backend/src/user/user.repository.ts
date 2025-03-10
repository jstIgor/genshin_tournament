import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { registerUserDto } from './dtos/register-user.dto';
import { User } from '@prisma/client';
import * as argon2 from 'argon2';
@Injectable()
export class UserRepository {
  constructor(private prisma: PrismaService) {}
  async createUser(dto: registerUserDto): Promise<User | void> {
    try {
      const hashPassword = await argon2.hash(dto.password)
      const user = await this.prisma.user.create({
        data: {
          passwordHash: hashPassword,
          name: dto.name,
        },
      });
      return user;
    } catch (error) {
      console.log(error);
    }
  }

  async findUserByName(nickname: string): Promise<User | null> {
    const user = await this.prisma.user.findUnique({
      where: {
        name: nickname,
      },
    });
    
    return user;
  }

  async findUserById(id: string) {
    return await this.prisma.user.findUnique({
      where: {
        id: id,
      },
    });
  }

}
