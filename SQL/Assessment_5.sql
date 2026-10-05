USE SKYTUS;
SHOW TABLES;
DROP TABLE user;
CREATE TABLE user_data(
   User_ID INT PRIMARY KEY,
   Email varchar(100) unique,
   Pass_word int not null
);
SELECT * FROM user_data;

CREATE TABLE Orders(
Order_ID INT PRIMARY KEY,
Order_Name varchar(100), User_ID INT,foreign key(User_ID) references user_data(User_ID)
);
SELECT * FROM Orders;

#INSERT VALUES 
#user_data table(
INSERT INTO user_data (User_ID,Email,Pass_word)
values
(7001,"xyz@gmail.com",1234),
(7002,"abc@gmail.com",5678),
(7003,"pqr@gmail.com",2435),
(7004,"klm@gmail.com",1111),
(7005,"xyyyz@gmail.com",2222),
(7006,"uvw@gmail.com",1114),
(7007,"jklm@gmail.com",4433);
#Ordder table
INSERT INTO Orders (Order_id,Order_Name)
values
(501,"SAMSUNG PHONE"),
(502,"HP-LAPTOP"),
(503,"BOAT HEADPHONE"),
(504,"DELL KEYBOARD AND MOUSE"),
(505,"MILTOM BOTTLE");

#CREATE INDEX ON EMAIL COLUMN
SHOW INDEX FROM user_data; #CHEAK INDEX IS WORK OR NOT
CREATE INDEX idx_Email ON user_data(Email);

#CREATE VIEW FOR USER ORDER DISPLAY SUMMRY
CREATE  VIEW ORDER_SUMMARY AS SELECT  Order_Name FROM Orders;
SELECT * FROM ORDER_SUMMARY; #FOR CHEAK VIEW 