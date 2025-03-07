import { PrismaClient } from "@prisma/client";

describe('PrismaService', () => {

  describe('PrismaService', () => {
    let prisma: PrismaClient;
  
    beforeAll(async () => {
      prisma = new PrismaClient();
      await prisma.$connect(); 
    });
  
    afterEach(async () => {
      await prisma.user.deleteMany();  
    });
  
    afterAll(async () => {
      await prisma.$disconnect();
    });
  
    describe('check connection', () => {
      it('should upsert a user', async () => {
        const user = {
          name: 'sadfg',
          passwordHash: 'dsfgfty45',
        };
  
        const newUser = await prisma.user.upsert({
          where: {
            name: user.name,
          },
          update: {
            passwordHash: user.passwordHash,
          },
          create: {
            name: user.name,
            passwordHash: user.passwordHash,
          },
        });
  
        expect(newUser).toHaveProperty('name', user.name);
        expect(newUser).toHaveProperty('passwordHash', user.passwordHash);
      });
    });
  });
});