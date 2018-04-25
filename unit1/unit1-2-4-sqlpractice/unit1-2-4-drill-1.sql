WITH r as
(SELECT
	date
FROM
	weather
WHERE Events = 'Rain'
GROUP BY 1)

SELECT 
	trip_id,
	duration,
	date(start_date) trip_date
FROM
	trips
JOIN
	r
ON
	r.date = trip_date
ORDER BY 
	duration DESC
LIMIT
	3
