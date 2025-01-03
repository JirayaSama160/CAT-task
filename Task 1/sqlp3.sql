SELECT manager_id AS name
FROM Employee
GROUP BY manager_id
HAVING COUNT(*) > 4;