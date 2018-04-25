WITH r as
(SELECT
	date
FROM
	weather
WHERE Events = 'Rain'
GROUP BY 1)

SELECT 
	MAX(duration),
	date(start_date) trip_date
FROM
	trips
JOIN
	r
ON
	r.date = trip_date
GROUP BY
	2
ORDER BY 
	trip_date ASC
