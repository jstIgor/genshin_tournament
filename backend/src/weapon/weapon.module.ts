import { Module } from '@nestjs/common';
import { WeaponService } from './weapon.service';
import { WeaponController } from './weapon.controller';
import { PrismaService } from 'src/prisma/prisma.service';

@Module({
  controllers: [WeaponController],
  providers: [WeaponService, PrismaService],
})
export class WeaponModule {}
