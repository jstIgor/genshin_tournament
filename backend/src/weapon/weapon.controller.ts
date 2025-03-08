import { Controller } from '@nestjs/common';
import { WeaponService } from './weapon.service';

@Controller('weapon')
export class WeaponController {
  constructor(private readonly weaponService: WeaponService) {}
}
