SELECT AVG(crop_yield) AS average_yield
FROM crop_yield_data
GROUP BY crop_type;

SELECT weather_condition, COUNT(*) AS occurrences
FROM weather_data
GROUP BY weather_condition;

SELECT c.crop_type, AVG(c.crop_yield) AS average_yield, w.weather_condition
FROM crop_yield_data c
JOIN weather_data w ON c.date = w.date
GROUP BY c.crop_type, w.weather_condition;

SELECT date, SUM(crop_yield) AS total_yield
FROM crop_yield_data
WHERE date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY date
ORDER BY date;