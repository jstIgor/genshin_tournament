import { Injectable } from "@nestjs/common";
import { UserRepository } from "./user.repository";

@Injectable()
export class UserPrivateSerivce {
  constructor(
    private userRepository: UserRepository
  ){}
}