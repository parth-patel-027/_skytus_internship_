#Query Optimization
use e_commerce;
SHOW TABLES; #TO SHOW ALL TABLES IN DATABASE.
select * from customers;
select * from order_items;

#OPRATION-1---------------------------------------------------
#ADD INDEX TO IMPROVE SEARCH ON ORDERS.Customer_ID
create index idx_Customer_ID on Orders(Customer_ID);
SHOW INDEX FROM Orders; #CHEAK INDEX IS WORK OR NOT

#OPRATION-2---------------------------------------------------
#USE EXPLAIN TO ANALYZE QUERY
EXPLAIN SELECT Name,City from customers where Customer_ID=1; #explain query flow

#OPRATION-3---------------------------------------------------
#OPTIMIZE SLOW JOIN QUERY
OPTIMIZE  table orders_items;

#OPRATION-4---------------------------------------------------
#Explain WHEN INDEX IS NOT  BE USE
EXPLAIN
SELECT *
FROM order_items
WHERE Product_ID = 1;