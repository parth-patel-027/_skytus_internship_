CREATE DATABASE BANK;
USE BANK;
SHOW tables;
CREATE TABLE Accounts(
   ID int primary KEY,
   Name VARCHAR(50),
   Balance INT   
);
SELECT * FROM Accounts;

#INSERT RECORD INTO ACCOUNTS---------------------------------------------------------------------------
INSERT INTO Accounts(ID,Name,Balance)
VALUES
(1,"PARTH PATEL",5000),
(2,"VANSH PATEL",4000),
(3,"MIT PATEL",3000);

#START TRANSACTION--------------------------------------------------------------------------------------
UPDATE Accounts 
SET Balance=Balance-2000
WHERE ID = 2;
UPDATE Accounts 
SET Balance=Balance+2000
WHERE ID = 3;

#ROLLBACK---------------------------------------------------------------------------------------------------
#ROLLBACK 1000 RUPEE FROM ID 1
START TRANSACTION;
UPDATE Accounts 
SET Balance=Balance+1000
WHERE ID =1;
rollback;
#ROLLBACK 1000 RUPEE FROM ID 2
START TRANSACTION;
UPDATE Accounts
SET Balance=Balance+1000
WHERE ID=2;
ROLLBACK;
SELECT * FROM Accounts;

#DEMONSTRTE TRANFER OF MONEY USING TRANSACTION--------------------------------------------------------------

START TRANSACTION;
#IT IS TEMPORY CHNAGES IT IS PERMENT AFTER COMMIIT
#SAND 1000 TO VANSH
UPDATE Accounts 
SET Balance=Balance-1000
WHERE ID = 1;

#RECIVE 1000 RUPEE FROM PARTH
UPDATE Accounts 
SET Balance=Balance+1000
WHERE ID = 2;

#COMMIT FOR PARMENT CHNAGE----------------------------------------------------------------------------------
COMMIT;