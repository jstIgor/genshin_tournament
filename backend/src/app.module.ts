import { Module } from '@nestjs/common';
import { UserModule } from './user/user.module';
import { PrismaModule } from './prisma/prisma.module';
import { ConfigModule } from '@nestjs/config';
import { CharacterModule } from './character/character.module';
import { WeaponModule } from './weapon/weapon.module';

@Module({
  imports: [UserModule, PrismaModule, ConfigModule.forRoot(), CharacterModule, WeaponModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
