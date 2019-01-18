DROP TABLE IF EXISTS "Children";
DROP TABLE IF EXISTS "Gifts";

CREATE TABLE "Children" (
  "Child_ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Name" TEXT NOT NULL,
  "Good" BIT NOT NUll
);

CREATE TABLE "Gifts" (
  "Gift_ID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Name" TEXT NOT NULL,
  "Delivered" BIT NOT NULL, 
  "Child_ID" INTEGER NOT NUll,
  FOREIGN KEY ("Child_ID")
  REFERENCES "Children"("Child_ID")
);


INSERT INTO Children
VALUES (null, "Bryan", 1);

INSERT INTO Children
VALUES (null, "Sally", 1);

INSERT INTO Gifts
VALUES (null, "Basket Ball", 1, 1);

INSERT INTO Gifts
VALUES (null, "Iphone", 0, 2);