import {
  BadGatewayException,
  BadRequestException,
  Body,
  Controller,
  Get,
  HttpCode,
  Post,
  Req,
  UseInterceptors,
} from '@nestjs/common';
import { UserRepository } from './user.repository';
import { registerUserDto } from './dtos/register-user.dto';
import { UserAuthService } from './user.auth.service';
import { TokenInterceptor } from 'src/interceptors/set-token.interceptor';
import { ApiOperation, ApiTags } from '@nestjs/swagger';
import { loginUserDto } from './dtos/login-user.dto';
import { Request, Response } from 'express';
import { UserAndToken } from './interfaces/user-token.interface';
import * as cookieParser from 'cookie-parser';
@ApiTags('users')
@Controller('user')
export class UserController {
  constructor(
    private readonly userService: UserRepository,
    private userAuthService: UserAuthService,
  ) {}
  @UseInterceptors(TokenInterceptor)
  @HttpCode(200)
  @Post('/register')
  async registerUser(@Body() dto: registerUserDto) {
    const userAndTokens = await this.userAuthService.register(dto);
    return userAndTokens;
  }
  @Post('/login')
  @UseInterceptors(TokenInterceptor)
  async Login(@Body() dto: loginUserDto) {
    return await this.userAuthService.login(dto);
  }
  @Get('/checkout')
  @UseInterceptors(TokenInterceptor)
  async checkout(@Req() req: Request) {
    const authHeader = req.headers.authorization;
    if (authHeader && authHeader.startsWith('Bearer ')) {
      const token = authHeader.split(' ')[1];
      return await this.userAuthService.checkout(token);
    } else {
      throw new BadRequestException('Authorization header is missing or invalid');
    }
  }
}
