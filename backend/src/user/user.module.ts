import { Module } from '@nestjs/common';
import { UserRepository } from './user.repository';
import { UserController } from './user.controller';
import { PrismaModule } from 'src/prisma/prisma.module';
import { PrismaService } from 'src/prisma/prisma.service';
import { UserAuthService } from './user.auth.service';
import { UserAdminService } from './user.admin.serice';
import { ConfigService } from '@nestjs/config';

@Module({
  controllers: [UserController],
  providers: [UserRepository, PrismaService, UserAuthService, UserAdminService, ConfigService],
  imports: [PrismaModule]
})
export class UserModule {}
