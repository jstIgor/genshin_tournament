import {
  Body,
  Controller,
  Get,
  HttpCode,
  Post,
  Req,
  UseInterceptors,
} from '@nestjs/common';
import { UserService } from './user.service';
import { registerUserDto } from './dtos/register-user.dto';
import { UserAuthService } from './user.auth.service';
import { TokenInterceptor } from 'src/interceptors/set-token.interceptor';
import { UserReponseDto } from './dtos/uesr-response.dto';

@Controller('user')
export class UserController {
  constructor(
    private readonly userService: UserService,
    private userAuthService: UserAuthService,
  ) {}
  @UseInterceptors(TokenInterceptor)
  @HttpCode(200)
  @ClearUserRes()
  @Post('/register')
  async registerUser(@Body() dto: registerUserDto) {
    console.log(dto);
    const userAndTokens = await this.userAuthService.register(dto);
    return userAndTokens 
  }
  @Get('/hello')
  async sayHello() {
    return 'hello';
  }
}
