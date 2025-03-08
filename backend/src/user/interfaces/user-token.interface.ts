import { User } from "@prisma/client";

export interface UserAndToken {
  user: User;
  token: string;
}