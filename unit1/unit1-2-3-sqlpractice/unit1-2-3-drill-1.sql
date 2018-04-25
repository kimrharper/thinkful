SELECT 
	Max("Max(MaxTemperatureF)"),
	Date

FROM 
	(SELECT
		Max(MaxTemperatureF),
		Date
	FROM
		weather
	GROUP by Date
	ORDER by MaxTemperatureF DESC)
