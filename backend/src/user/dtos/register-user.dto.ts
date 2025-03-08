import { IsString } from "class-validator";

export class registerUserDto {
  @IsString()
  password: string
  @IsString()
  name: string
}