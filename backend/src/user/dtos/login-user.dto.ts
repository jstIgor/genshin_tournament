import { IsString } from "class-validator";

export class loginUserDto {
  @IsString()
  password: string
  @IsString()
  name: string
}