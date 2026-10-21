-- =====================================MESS MANAGEMENT SYSTEM=================================================================

CREATE DATABASE MESS_MANAGEMENT_SYSTEM;
USE MESS_MANAGEMENT_SYSTEM;

-- CREATE STUDENT TABLE---------------------------------------------------------------------------------- 

CREATE TABLE STUDENT_DATA(
 STUDENT_ID INT PRIMARY KEY,
 STUDENT_NAME VARCHAR(50),
 GENDER VARCHAR(10),
 COURSE VARCHAR(20),
 PHONE VARCHAR(15),
 JOIN_DATE DATE
);
SELECT * FROM STUDENT_DATA;
INSERT INTO STUDENT_DATA
VALUES
(1, 'Amit', 'Male', 'CE', '9876543210', '2026-01-10'),
(2, 'Parth', 'Male', 'IT', '9876543211', '2026-02-15'),
(3, 'Neha', 'Female', 'CE', '9876543212', '2026-01-20'),
(4, 'Rahul', 'Male', 'IT', '9876543213', '2026-03-01'),
(5, 'Priya', 'Female', 'CE', '9876543214', '2026-02-05'),
(6, 'Vansh', 'Male', 'IT', '9876543215', '2026-04-10'),
(7, 'Kavya', 'Female', 'CE', '9876543216', '2026-03-15'),
(8, 'Meet', 'Male', 'IT', '9876543217', '2026-05-01'),
(9, 'Riya', 'Female', 'CE', '9876543218', '2026-04-20'),
(10, 'Dhruv', 'Male', 'IT', '9876543219', '2026-05-10');

-- CREATE TABLE FOR THE MESS_PLAN DATA-------------------------------------------------------------

CREATE TABLE MESS_PLAN_DATA(
  PLAN_ID INT PRIMARY KEY,
  PLAN_NAME VARCHAR(30) NOT NULL,
  MONTHLY_FEE DECIMAL(10,2) NOT NULL,
  DURATION_MONTH INT NOT NULL
);
SELECT * FROM MESS_PLAN_DATA;
INSERT INTO MESS_PLAN_DATA 
VALUES
(1, 'Basic', 2500, 1),
(2, 'Standard', 3500, 1),
(3, 'Premium', 4500, 1),
(4, 'Quarterly', 9000, 3),
(5, 'Half_Yearly', 17000, 6);

-- CREATE TABLE FOR SUSCRIPTION DATA -----------------------------------------------------------------------------

CREATE TABLE SUSCRIPTION(
SUSCRIPYION_ID INT PRIMARY KEY,
STUDENT_ID INT NOT NULL,
PLAN_ID INT NOT NULL,
START_DATE DATE,
END_DATE DATE,
Status_ varchar(40),
 FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT_DATA(Student_ID),
 FOREIGN KEY (PLAN_ID) REFERENCES MESS_PLAN_DATA(PLAN_ID)
);
ALTER TABLE SUSCRIPTION RENAME COLUMN SUSCRIPYION_ID TO SUSCRIPTION_ID;

SELECT * FROM SUSCRIPTION;
INSERT INTO SUSCRIPTION 
VALUES (1, 1, 2, '2026-01-10', '2026-02-09', 'Expired'),
(2, 2, 3, '2026-10-01', '2026-10-31', 'Active'),
(3, 3, 1, '2026-10-01', '2026-10-31', 'Active'),
(4, 4, 2, '2026-09-01', '2026-09-30', 'Expired'),
(5, 5, 4, '2026-08-01', '2026-10-31', 'Active'),
(6, 6, 3, '2026-10-05', '2026-11-04', 'Active'),
(7, 7, 1, '2026-10-01', '2026-10-31', 'Active'),
(8, 8, 5, '2026-07-01', '2026-12-31', 'Active'),
(9, 9, 2, '2026-10-01', '2026-10-31', 'Active'),
(10, 10, 3, '2026-09-01', '2026-09-30', 'Expired');

-- CREATE TABLE FOR PAYMENTS ----------------------------------------------------------------------------------------

CREATE TABLE PAYMENT_DATA(
  PAYMENT_ID INT PRIMARY KEY,
  SUSCRIPTION_ID INT NOT NULL,
  AMOUNT DECIMAL(10,2) NOT NULL,
  PAYMENT_DATE DATE,
  PAYMENT_METHOD VARCHAR(30),
  PAYMENT_STATUS VARCHAR (30)
);
SELECT * FROM PAYMENT_DATA;
INSERT INTO PAYMENT_DATA
VALUES
(1, 1, 3500, '2026-01-10', 'UPI', 'Paid'),
(2, 2, 4500, '2026-10-01', 'UPI', 'Paid'),
(3, 3, 2500, '2026-10-01', 'Cash', 'Paid'),
(4, 4, 3500, '2026-09-01', 'Card', 'Paid'),
(5, 5, 9000, '2026-08-01', 'UPI', 'Paid'),
(6, 6, 4500, '2026-10-05', 'UPI', 'Paid'),
(7, 7, 2500, '2026-10-01', 'Cash', 'Pending'),
(8, 8, 17000, '2026-07-01', 'Card', 'Paid'),
(9, 9, 3500, '2026-10-01', 'UPI', 'Pending'),
(10, 10, 4500, '2026-09-01', 'Cash', 'Paid');


-- CREATE TABLE FOR THE MENU-----------------------------------------------------------------------

CREATE TABLE MENU(
MENU_ID INT PRIMARY KEY,
ITEM_NAME VARCHAR(30) NOT NULL,
MEAL_TYPE VARCHAR(10),
PRICE DECIMAL(10,2) NOT NULL,
AVALIABLE VARCHAR(10)
);
SELECT * FROM MENU;
INSERT INTO MENU 
VALUES
(1, 'Poha', 'Breakfast', 30, 'Yes'),
(2, 'Tea', 'Breakfast', 10, 'Yes'),
(3, 'Roti Sabzi', 'Lunch', 70, 'Yes'),
(4, 'Dal Rice', 'Lunch', 60, 'Yes'),
(5, 'Khichdi', 'Dinner', 50, 'Yes'),
(6, 'Paneer Curry', 'Dinner', 100, 'Yes'),
(7, 'Sandwich', 'Breakfast', 40, 'No'),
(8, 'Biryani', 'Dinner', 120, 'Yes'),
(9, 'Dhokla', 'Breakfast', 25, 'Yes'),
(10, 'Dal Khichdi', 'Dinner', 65, 'Yes');


-- CRETATE TABLE FOR THE MEAL RECORDS

CREATE TABLE MEAL_RECORDS(
 RECORD_ID INT PRIMARY KEY,
 STUDENT_ID INT NOT NULL,
 MENU_ID INT NOT NULL,
 MEAL_DATE DATE,
 QUANTITY INT NOT NULL
);

SELECT * FROM MEAL_RECORDS;
INSERT INTO Meal_Records
(Record_ID, Student_ID, Menu_ID, Meal_Date, Quantity)
VALUES
(1, 1, 1, '2026-10-10', 1),
(2, 2, 3, '2026-10-10', 1),
(3, 3, 4, '2026-10-10', 1),
(4, 4, 5, '2026-10-10', 1),
(5, 5, 6, '2026-10-11', 1),
(6, 6, 8, '2026-10-11', 1),
(7, 7, 2, '2026-10-11', 2),
(8, 8, 9, '2026-10-12', 1),
(9, 9, 10, '2026-10-12', 1),
(10, 10, 3, '2026-10-12', 2),
(11, 1, 4, '2026-10-12', 1),
(12, 2, 6, '2026-10-13', 1),
(13, 3, 1, '2026-10-13', 2),
(14, 5, 8, '2026-10-13', 1),
(15, 6, 5, '2026-10-13', 1);

#====================================================================================================================================================================

-- 1.Display all student details.
SELECT * FROM STUDENT_DATA;

-- 2.Find students who have active subscriptions.
SELECT STUDENT_NAME,Status_ FROM
 STUDENT_DATA AS D JOin SUSCRIPTION AS S
 ON D.STUDENT_ID = S.STUDENT_ID WHERE Status_ ="Active";
 
 -- 3.Find mess plans with a monthly fee greater than ₹3,000.
 SELECT PLAN_ID,PLAN_NAME,MONTHLY_FEE FROM MESS_PLAN_DATA WHERE MONTHLY_FEE >3000;
 
 -- 4.Find the names of students whose payments are pending, along with the payment amounts.
 SELECT D.STUDENT_NAME,P.PAYMENT_STATUS,P.AMOUNT 
 FROM STUDENT_DATA as D join SUSCRIPTION AS S
    ON D.STUDENT_ID = S.STUDENT_ID 
 JOIN PAYMENT_DATA AS P 
    ON P.SUSCRIPTION_ID = s.SUSCRIPTION_ID
 WHERE P.PAYMENT_STATUS='Pending';
 
 -- 5.Count the number of subscriptions for each mess plan.

 SELECT  M.PLAN_NAME ,COUNT(S.PLAN_ID ) FROM 
 SUSCRIPTION AS S JOIN MESS_PLAN_DATA AS M
 ON 
    S.PLAN_ID = M.PLAN_ID
 GROUP BY M.PLAN_NAME;
 
 -- 6.Calculate the total amount collected through each payment method.
SELECT SUM(AMOUNT),PAYMENT_METHOD  FROM PAYMENT_DATA GROUP BY PAYMENT_METHOD;

-- 7.Display each student's name, plan name, and subscription status.
SELECT SD.STUDENT_NAME ,PD.PLAN_NAME, S.Status_ FROM
STUDENT_DATA AS SD JOIN SUSCRIPTION AS S
ON
   SD.STUDENT_ID = S.STUDENT_ID 
JOIN MESS_PLAN_DATA AS PD
ON 
   PD.PLAN_ID = S.PLAN_ID;   
   
-- 8.Find the most expensive menu item and display its name and price.  
SELECT ITEM_NAME,PRICE FROM MENU ORDER BY PRICE DESC LIMIT 1;

-- 9.Calculate the total quantity consumed for each meal item.
SELECT M.MENU_ID,M.ITEM_NAME,SUM(R.QUANTITY) FROM MENU AS M JOIN MEAL_RECORDS AS R
ON 
  M.MENU_ID = R.MENU_ID 
GROUP BY MENU_ID,ITEM_NAME 
ORDER BY MENU_ID ASC;  

-- 10.Find all payments made in October 2026. Display the payment details.
SELECT PAYMENT_ID,AMOUNT,PAYMENT_METHOD,PAYMENT_DATE 
 FROM PAYMENT_DATA WHERE PAYMENT_DATE >="2026-10-01" AND "2026-11-01"; -- USING DATE RANGE 
 
 -- 11.Find students subscribed to the most expensive mess plan.  
 -- Display student name,plan name, monthly fee, and a CASE-generated category: Premium
 -- if the fee is above ₹3,000, otherwise Regular.
  
  SELECT D.STUDENT_NAME,
  M.PLAN_NAME,
  M.MONTHLY_FEE,
  M.PLAN_ID,
   CASE 
	WHEN M.MONTHLY_FEE >3000 THEN 'Premium'
	ELSE 'Regular' END AS PLAN_CATEGORY
  FROM 
  MESS_PLAN_DATA AS M
  JOIN SUSCRIPTION AS S
     ON M.PLAN_ID = S.PLAN_ID 
  JOIN  STUDENT_DATA AS D
      ON S.STUDENT_ID = D.STUDENT_ID;
    
    -- 12.Display every student and their total paid amount, 
    -- including students with no paid payments (show 0). 
    -- Then display only students whose total paid amount is greater than ₹5,000.
      
    SELECT
    D.STUDENT_ID,
    D.STUDENT_NAME,
    COALESCE(SUM(      -- if value is null then show default value 
        CASE
            WHEN P.PAYMENT_STATUS = 'Paid'
            THEN P.AMOUNT
            ELSE 0
        END
    ), 0) AS TOTAL_PAID_AMOUNT
FROM STUDENT_DATA AS D
LEFT JOIN SUSCRIPTION AS S
    ON D.STUDENT_ID = S.STUDENT_ID
LEFT JOIN PAYMENT_DATA AS P
    ON P.SUSCRIPTION_ID = S.SUSCRIPTION_ID
GROUP BY D.STUDENT_ID, D.STUDENT_NAME
HAVING COALESCE(SUM(
    CASE
        WHEN P.PAYMENT_STATUS = 'Paid'
        THEN P.AMOUNT
        ELSE 0
    END
), 0) > 5000;
   -- 13.Create an index named idx_payment_status on 
   -- the PAYMENT_STATUS column of the PAYMENT_DATA table.
   -- Then display all indexes of that table.
    
    CREATE INDEX IDX_PAYMENT_STATUS ON PAYMENT_DATA(PAYMENT_STATUS);
    SHOW INDEX FROM PAYMENT_DATA ;
   
   
   -- 14.Create a view named PENDING_PAYMENTS that displays PAYMENT_ID, AMOUNT, and PAYMENT_DATE
   -- for payments whose status is 'Pending'. Then display all records from the view.
CREATE VIEW PENDING_PAYMENTS AS
SELECT PAYMENT_ID, AMOUNT, PAYMENT_DATE
FROM PAYMENT_DATA
WHERE PAYMENT_STATUS = 'Pending';

SELECT * FROM PENDING_PAYMENTS;

-- 15.Display each mess plan's name, total number of subscriptions,
-- and number of active subscriptions. Include plans that have no subscriptions.

SELECT M.PLAN_NAME,count(S.SUSCRIPTION_ID) AS TOTAL_SUSCRIPTION , 
SUM(
    CASE 
        WHEN S.Status_ = 'Active' then 1
		ELSE 0
        END
        ) AS ACTIVE_SUSCRIPTION 
	FROM MESS_PLAN_DATA AS M
     LEFT JOIN SUSCRIPTION AS S 
       ON M.PLAN_ID = S.PLAN_ID
       GROUP BY M.PLAN_ID, M.PLAN_NAME;
  
  #========================OPTIMIZE AT LEAST 3 QUERY===============================================
  
  -- 1.EXPLAIN
--   Use EXPLAIN to analyze a query that finds all payments with PAYMENT_STATUS = 'Pending'.
  
  EXPLAIN SELECT PAYMENT_STATUS FROM PAYMENT_DATA WHERE PAYMENT_STATUS ='Pending';
  
  
  -- 2.SHOW INDEX
--  Write a query to display all indexes created on the PAYMENT_DATA table. T
 
 SHOW INDEX FROM PAYMENT_DATA;
 
 -- 3.CREATE INDEX
-- Create an index named IDX_PAYMENT_DATE on the PAYMENT_DATE column of the PAYMENT_DATA table.
 
 CREATE INDEX IDX_PAYMENT_DATE ON PAYMENT_DATA(PAYMENT_DATE);
