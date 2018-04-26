
-- Counted total number of rentals in each neighbourhood to find the most popular area


SELECT
	neighbourhood,
	COUNT(neighbourhood) total_count
FROM
	listings
GROUP BY 1
ORDER BY total_count DESC
LIMIT 1
