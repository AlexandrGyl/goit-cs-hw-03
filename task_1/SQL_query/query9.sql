SELECT s.name, COUNT(t.id)
FROM tasks t
JOIN status s ON t.status_id = s.id
GROUP BY s.name;