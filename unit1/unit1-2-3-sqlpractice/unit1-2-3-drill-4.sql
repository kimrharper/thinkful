SELECT
    AVG(duration),
	end_station
	
FROM
    trips
	
GROUP BY end_station