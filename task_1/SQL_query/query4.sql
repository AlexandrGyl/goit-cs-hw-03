SELECT *
FROM tasks
WHERE status_id NOT IN (SELECT id FROM status WHERE name IN ('new', 'in progress', 'completed'));