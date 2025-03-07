import { Module } from '@nestjs/common';
import { UserService } from './user.service';
import { UserController } from './user.controller';
import { PrismaModule } from 'src/prisma/prisma.module';
import { PrismaService } from 'src/prisma/prisma.service';
import { UserAuthService } from './user.auth.service';

@Module({
  controllers: [UserController],
  providers: [UserService, PrismaService, UserAuthService],
  imports: [PrismaModule]
})
export class UserModule {}
