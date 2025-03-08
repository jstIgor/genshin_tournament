import { Injectable, NotFoundException } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { registerUserDto } from './dtos/register-user.dto';
import { User } from '@prisma/client';
import * as argon2 from 'argon2';
@Injectable()
export class UserAdminService {
  constructor(private prisma: PrismaService) {}
  //  async giveRolePlayerToUser(userId): Promise<Vpid> {
  //   const userUpdated = await this.prisma.user.update({
  //     where: {
  //       id: userId,
  //     },
  //     data: { role: 'PLAYER' },
  //   });
  //   if(!userUpdated) {
  //     throw new NotFoundException(`Пользователь с айди: ${userId} не найден`)
  //   }
  //   return userUpdated;
  // }

  //  async giveRoleUserToUser(userId): Promise<User> {
  //   const userUpdated = await this.prisma.user.update({
  //     where: {
  //       id: userId,
  //     },
  //     data: { role: 'USER' },
  //   });
  //   if(!userUpdated) {
  //     throw new NotFoundException(`Пользователь с айди: ${userId} не найден`)
  //   }
  //   return userUpdated;
  // }

}
