-- CreateTable
CREATE TABLE "user" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "password_hash" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "role" TEXT NOT NULL DEFAULT 'PLAYER'
);

-- CreateTable
CREATE TABLE "character" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "picture" TEXT NOT NULL DEFAULT 'no-image-hero.png',
    "score" INTEGER NOT NULL,
    "userId" TEXT,
    CONSTRAINT "character_userId_fkey" FOREIGN KEY ("userId") REFERENCES "user" ("id") ON DELETE SET NULL ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "weapon" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "score" INTEGER NOT NULL,
    "userId" TEXT,
    CONSTRAINT "weapon_userId_fkey" FOREIGN KEY ("userId") REFERENCES "user" ("id") ON DELETE SET NULL ON UPDATE CASCADE
);
