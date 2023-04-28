SELECT job_title, COUNT(*) AS employee_count
FROM employee
GROUP BY job_title;