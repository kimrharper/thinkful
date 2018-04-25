-- Set up the CTE to create a "locations" table.
WITH
    locations
AS (
    -- A simple query to get the averages of lat and long on a city level.
    SELECT
        city,
        AVG(lat) lat,
        AVG(long) long
    FROM
        stations
    GROUP BY 1
)

SELECT
    l.city,
    l.lat,
    l.long,
    COUNT(*)
FROM
    locations l
	
-- We need an intermediate join to go from locations to stations 
-- because the trips table does not have a "city" column.
JOIN
    stations s
ON
    l.city = s.city
JOIN
    trips t
ON
    t.start_station = s.name
GROUP BY 1
