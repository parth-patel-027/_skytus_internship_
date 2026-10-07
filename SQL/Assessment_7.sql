CREATE DATABASE E_COMMERCE;
USE E_COMMERCE;
SHOW TABLES;

#Customer DATA Table
CREATE TABLE Customers(
 Customer_ID INT primary KEY,
 Name VARCHAR(100),
 City VARCHAR(100)
);
#INSERT DATA
INSERT INTO Customers(Customer_ID,Name,City)
VALUES
(1, 'Parth Patel', 'Surat'),
(2, 'Amit Shah', 'Ahmedabad'),
(3, 'Rahul Mehta', 'Vadodara'),
(4, 'Vansh Patel', 'Surat'),
(5, 'Neel Joshi', 'Rajkot'),
(6, 'Jay Patel', 'Ahmedabad'),
(7, 'Karan Shah', 'Mumbai'),
(8, 'Dev Patel', 'Pune'),
(9, 'Harsh Mehta', 'Surat'),
(10, 'Ravi Shah', 'Vadodara');

SELECT * FROM Customers;

#Product data table

CREATE TABLE Products(
     Product_ID INT PRIMARY KEY,
     Product_Name VARCHAR(50),
     Price INT 
);
SELECT * FROM Products;

#INSERT DATA OF PRODUCT
INSERT INTO Products(Product_ID,Product_Name,Price)
values
(101, 'Laptop', 55000),
(102, 'Mobile', 25000),
(103, 'Headphones', 3000),
(104, 'Keyboard', 2000),
(105, 'Mouse', 1200),
(106, 'Monitor', 15000),
(107, 'Smart Watch', 8000),
(108, 'Tablet', 30000);


#order
CREATE TABLE Orders(
  Order_ID INT PRIMARY KEY,
  Customer_ID INT, FOREIGN KEY(Customer_ID) REFERENCES Customers(Customer_ID),
  Order_Date date ,
  Amount INT
);
SELECT * FROM Orders;
#insert data into orders data
INSERT INTO Orders(Order_ID,Customer_ID,Order_Date,Amount)
values
(1001, 1, '2026-01-05', 55000),
(1002, 2, '2026-01-10', 25000),
(1003, 3, '2026-01-15', 30000),
(1004, 1, '2026-02-05', 30000),
(1005, 4, '2026-02-12', 55000),
(1006, 5, '2026-02-20', 15000),
(1007, 2, '2026-03-03', 60000),
(1008, 6, '2026-03-10', 25000),
(1009, 3, '2026-03-18', 55000),
(1010, 1, '2026-04-02', 80000),
(1011, 4, '2026-04-08', 30000),
(1012, 5, '2026-04-15', 25000),
(1013, 7, '2026-05-05', 55000),
(1014, 8, '2026-05-12', 30000),
(1015, 2, '2026-05-20', 80000),
(1016, 9, '2026-06-01', 60000),
(1017, 1, '2026-06-10', 30000),
(1018, 3, '2026-06-15', 25000);


#ORDER items DATA Table
CREATE TABLE Order_items(
   Order_id INT,
   Product_ID INT,
   Quantity INT,
   primary key (Order_id,Product_id),
   FOREIGN KEY (Order_id) references orders(Order_id),
   FOREIGN KEY (product_id) REFERENCES products(product_id)
);
SELECT * FROM Order_items;
#insert data orders item

INSERT INTO Order_items(Order_id,Product_ID,Quantity)
values
(1001, 101, 1),
(1002, 102, 1),
(1003, 108, 1),
(1004, 108, 1),
(1005, 101, 1),
(1006, 106, 1),
(1007, 102, 2),
(1008, 102, 1),
(1009, 101, 1),
(1010, 101, 1),
(1010, 102, 1),
(1011, 108, 1),
(1012, 106, 1),
(1013, 101, 1),
(1014, 108, 1),
(1015, 101, 1),
(1015, 102, 1),
(1016, 102, 1),
(1017, 108, 1),
(1018, 102, 1);

#OPRATION-1-----------------------------------------------------------------------------
#TOTAL OREDR PER CUSTOMER
SELECT Customer_ID,count(Order_id) from orders;


#OPRATION-2-----------------------------------------------------------------------------
#customer who never place order
SELECT Customers.Customer_ID 
FROM 
Customers LEFT JOIN Orders
on Customers.Customer_ID = Orders.Customer_ID 
where Orders.Order_id is null;

#OPRATION-3-----------------------------------------------------------------------------
#FIND HIGHEST SELLING  PRODUCTS
SELECT  Product_ID,sum(Quantity) as a 
from Order_items 
group by Product_ID
having
sum(Quantity)=(SELECT MAX(A) FROM 
(SELECT  Product_ID,sum(Quantity) as a 
from Order_items 
group by Product_ID )AS A
);
  
#OPRATION-4--------------------------------------------------------------------------------
#DISPLAY MONTHLY SELLING REPORT
SELECT month(Order_Date),sum(Amount) from orders group by month(Order_Date);

#OPRATION-5--------------------------------------------------------------------------------
#Customer total Purchase > 50,000₹
SELECT Customer_ID,sum(Amount) as total FROM Orders 
group by Customer_ID HAVING total>50000;

#OPRATION-6-------------------------------------------------------------------------------
#TOP 3 CITY BY REVNUE
SELECT c.City,sum(o.Amount) as revenue FROM
 Orders as o join customers as c
 on c.Customer_ID= o.Customer_ID
group by c.City
order by revenue 
limit 3
;
