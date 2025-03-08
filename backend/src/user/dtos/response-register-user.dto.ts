import { Exclude, Expose } from "class-transformer";
import { IsOptional, IsString } from "class-validator";
@Exclude()
export class UserRegistratedResponse {
  @Expose()
  @IsString()
  name: string
  @Expose()
  @IsString()
  id: string 
}