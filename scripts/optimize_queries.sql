-- Optimize SQL queries for better performance

-- Example of optimizing a query by using indexes
CREATE INDEX idx_crop_yield ON crop_yield_data (crop_type, year);

-- Example of optimizing a query by rewriting it
SELECT crop_type, AVG(yield) AS average_yield
FROM crop_yield_data
WHERE year >= 2010
GROUP BY crop_type
ORDER BY average_yield DESC;

-- Example of optimizing a join query
SELECT w.date, w.temperature, c.crop_type, AVG(c.yield) AS average_yield
FROM weather_data w
JOIN crop_yield_data c ON w.date = c.date
WHERE w.temperature > 20
GROUP BY w.date, w.temperature, c.crop_type
ORDER BY average_yield DESC;