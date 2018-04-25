SELECT
	stations.dockcount,
	stations.name,
	COUNT(trips.start_station) trip_count
FROM 
	stations
JOIN 
	trips
ON 
	stations.name = trips.start_station
GROUP BY 
	1,2
ORDER BY
	dockcount DESC