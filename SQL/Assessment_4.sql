USE company_db;
SHOW DATABASES ;
SELECT * FROM employees;
SELECT * FROM departments;
#find the employe earning more then avg salary
SELECT emp_name, salary from employees  where salary >( select  AVG(salary) FROM employees);

# Find Department with highest salary 
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC
LIMIT 1;

#display employee with second highest salary 
SELECT emp_name, salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;

#display emplolyee working in same department as amit
SELECT emp_name, dept_id
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);