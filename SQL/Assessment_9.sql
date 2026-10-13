#SQL CODING TEST 

CREATE DATABASE Employees;
use Employees;

create table Employees_data(
 Employee_ID int primary key,
 Employee_Name varchar(50),
 Salary int,
 Hire_Date date,
 Department_ID Int,
 Email varchar(70)
);

INSERT INTO Employees_data 
values
(1, 'Amit', 80000, '2022-01-15', 1, 'amit@gmail.com'),
(2, 'Parth', 60000, '2025-06-10', 2, 'parth@gmail.com'),
(3, 'Vansh', 80000, '2024-03-20', 1, 'vansh@gmail.com'),
(4, 'Rahul', 50000, '2025-08-12', 2, 'rahul@gmail.com'),
(5, 'palak', 70000, '2023-11-05', 3, 'palak@gmail.com'),
(6, 'Karan', 60000, '2025-04-18', 1, 'karan@gmail.com'),
(7, 'panthi', 90000, '2021-09-25', 3, 'panthi@gmail.com'),
(8, 'Jay', 50000, '2025-07-01', 2, 'jay@gmail.com'),
(9, 'meghna', 75000, '2024-12-10', 1, 'meghna@gmail.com'),
(10, 'Dev', 70000, '2025-05-15', 3, 'dev@gmail.com');

INSERT INTO Employees_data
(Employee_ID, Employee_Name, Salary, Hire_Date, Department_ID, Email)
VALUES
(11, 'Ravi', 55000, '2026-04-20', 1, 'ravi@gmail.com'),
(12, 'Neha', 65000, '2026-05-15', 2, 'neha@gmail.com'),
(13, 'Meet', 70000, '2026-06-10', 3, 'meet@gmail.com'),
(14, 'Kavya', 60000, '2026-08-05', 1, 'kavya@gmail.com'),
(15, 'Dhruv', 75000, '2026-09-20', 2, 'dhruv@gmail.com'),
(16, 'Krish', 50000, '2026-10-01', 3, 'krish@gmail.com');

#TABLE-2 Employee_Backup

CREATE TABLE Employee_backup(
     Employee_ID int,
     Employee_Name varchar(50),
     Salary int
);

select * from Employee_Backup;
insert into Employee_backup(Employee_ID,Employee_Name,Salary)
values
(1, 'Amit', 80000),
(3, 'Vansh', 80000),
(5, 'Neha', 70000),
(7, 'Priya', 90000),
(9, 'Riya', 75000),
(11, 'Meet', 55000);

#TEST QUERY-1-----------------------------------------------
# write a query to find Nth Highest salary

SELECT distinct Salary from
Employees_data  
order by Salary
 desc limit 1 
 offset 1; -- skip 1st value
 
 #TEST QUERY-2-----------------------------------------------
 -- REMOVE DUPLICATE RECORDS
 
 WITH DUPLICATE_REMOVE AS 
 (
 SELECT *,
 ROW_NUMBER() OVER 
 (PARTITION BY Department_ID 
  order by Department_Id )
 as duplicate_department 
 from employees_data
 )
 select * from DUPLICATE_REMOVE
 WHERE duplicate_department >1;

#TEST QUERY-3-------------------------------------------------
-- FIND A RECORDS COMMON IN TWO TABLE

SELECT e.Employee_Name,e.Salary from
 Employees_Data as e join Employee_Backup as b
 on e.Employee_Id = b.Employee_Id;
 
 
 #TEST QUERY-3----------------------------------------------
 -- FIND EMPLOYEE HIRED IN LAST 6 MONTH
 
 SELECT Employee_Name, month(Hire_Date)
 from Employees_Data
 where Hire_Date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
  AND Hire_Date <= CURDATE();
 
#TEST QUERY-4-----------------------------------------------
-- FIND A CONTINIOUS DUPLICATE VALUES
SELECT
    Employee_ID,
    Salary,
    LAG(Salary) OVER (ORDER BY Employee_ID) AS Previous_Salary
FROM Employees_Data;
