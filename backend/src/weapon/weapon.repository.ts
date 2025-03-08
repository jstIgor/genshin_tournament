import { Injectable } from "@nestjs/common";
import { Weapon } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";

@Injectable()
export class WeaponRepository {
  constructor(private prisma: PrismaService){}

  async getAllWeapons(): Promise<Weapon[]>{
    return await this.prisma.weapon.findMany();
  }

  async addWeapon(): Promise<Weapon>{
    return await this.prisma.weapon.create({
      data: {
        
      }
    })
  }
}