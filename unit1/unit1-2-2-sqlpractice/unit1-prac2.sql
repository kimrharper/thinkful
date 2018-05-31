SELECT
    trip_id, duration
FROM
    trips
WHERE
    duration > 500
Order by duration desc