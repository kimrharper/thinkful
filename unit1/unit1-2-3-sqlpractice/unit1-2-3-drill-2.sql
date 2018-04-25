SELECT
	start_station station_name,
    COUNT(*) start_station 
FROM
    trips
GROUP by start_station