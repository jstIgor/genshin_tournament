import {
  Injectable,
  NestInterceptor,
  ExecutionContext,
  CallHandler,
} from '@nestjs/common';
import { User } from '@prisma/client';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { UserReponseDto } from 'src/user/dtos/uesr-response.dto';

@Injectable()
export class ClearUserResInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    return next.handle().pipe(
      map((data) => {
        if (data && data.user) {
          const { extractedUser }: User = data
          const cleanedUser = new UserReponseDto(nickname: extractedUser., id: extractedUser.id)
        }
        return data;
      }),
    );
  }
}
