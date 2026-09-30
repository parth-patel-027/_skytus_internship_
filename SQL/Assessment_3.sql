CREATE DATABASE company_db;
USE company_db;
SHOW DATABASES;
CREATE TABLE employees(
 employe_id INT,
 emp_name varchar(100),
 dept_id int,
 salary int
);
SELECT * FROM employees;

CREATE TABLE departments(
    dept_id int,
    dept_name varchar(100)
);
SELECT * FROM departments;

INSERT INTO employees(employe_id,emp_name,dept_id,salary) 
VALUES
(1,"parth",101,50000),
(2,"vansh",102,40000),
(3,"nelson",103,60000),
(4,"mit",104,340000),
(5,"ronit",105,79000);

insert into employees(employe_id,emp_name,dept_id,salary)
value(6,"keyur",106,2000)
;

INSERT INTO departments (dept_id,dept_name)
values
 (101,"production"),
 (102,"finance"),
 (103,"selling"),
 (104,"social media"),
 (102,"finance");

#Display employee name with department name
SELECT e.emp_name,d.dept_name from employees  e join departments  d on e.dept_id = d.dept_id;

#Display department wise total  salary
SELECT d.dept_name, sum(e.salary) from employees e join departments d on e.dept_id = d.dept_id group by d.dept_name ;

#Display dipartment name which has a more then 2 employees
SELECT d.dept_name, count(e.emp_name) as employee_count from  employees e
 join departments d on e.dept_id = d.dept_id 
 group by d.dept_name 
 having count(e.emp_name) >2;

#Display employe without department
SELECT e.emp_name 
from
employees as e left join departments as d 
on e.dept_id = d.dept_id 
where d.dept_id is null; 

