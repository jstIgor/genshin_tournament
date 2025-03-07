import { User } from "@prisma/client"

interface UserRes {
  nickname: string,
  id: string
}
export class UserReponseDto implements UserRes {
  constructor(
    user: User
  ) {
    this.nickName = user.name,
    this.id = user.id
  }
}