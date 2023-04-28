SELECT first_name, last_name, job_title, department_id
FROM employee
JOIN department ON employee.department_id = department.department_id
WHERE city = 'London';