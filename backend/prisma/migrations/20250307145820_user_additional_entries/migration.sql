-- CreateTable
CREATE TABLE "Screenshot" (
    "name" TEXT NOT NULL,
    "userid" TEXT NOT NULL,
    CONSTRAINT "Screenshot_userid_fkey" FOREIGN KEY ("userid") REFERENCES "user" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- RedefineTables
PRAGMA defer_foreign_keys=ON;
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_user" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "password_hash" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "role" TEXT DEFAULT 'PLAYER'
);
INSERT INTO "new_user" ("id", "name", "password_hash", "role") SELECT "id", "name", "password_hash", "role" FROM "user";
DROP TABLE "user";
ALTER TABLE "new_user" RENAME TO "user";
CREATE UNIQUE INDEX "user_name_key" ON "user"("name");
PRAGMA foreign_keys=ON;
PRAGMA defer_foreign_keys=OFF;

-- CreateIndex
CREATE UNIQUE INDEX "Screenshot_userid_key" ON "Screenshot"("userid");
