SELECT
	status.station_id,
	stations.name,
	COUNT(CASE WHEN docks_available=0 then 1 END) emptystatus
FROM 
	status
JOIN 
	stations
ON 
	stations.station_id = status.station_id
GROUP BY 
	1
ORDER BY 
	empty_count DESC