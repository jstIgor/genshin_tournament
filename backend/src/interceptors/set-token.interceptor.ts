import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { Response } from 'express';
import { UserRegistratedResponse } from 'src/user/dtos/response-register-user.dto';
import { plainToInstance } from 'class-transformer';
import { UserAndToken } from 'src/user/interfaces/user-token.interface';

@Injectable()
export class TokenInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    const ctx = context.switchToHttp();
    const response = ctx.getResponse<Response>();

    return next.handle().pipe(
      map((data: UserAndToken | any) => {
        if (data?.token) {
          response.setHeader('Authorization', `Bearer ${(data as UserAndToken).token}`);
        }

        if (data?.user) {
          const filteredEntriesUser = plainToInstance(UserRegistratedResponse, data.user);
          return {
            ...filteredEntriesUser,
          };
        }

        return data;
      }),
      catchError((error) => {
        // Логируем ошибку и передаём её дальше
        console.error('Error:', error);
        return throwError(() => error);
      }),
    );
  }
}