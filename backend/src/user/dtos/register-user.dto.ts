import { IsString } from "class-validator";

export class registerUserDto {
  @IsString()
  password: string
  @IsString()
  nickName: string
}