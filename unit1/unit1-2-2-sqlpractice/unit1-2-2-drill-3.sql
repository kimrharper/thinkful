SELECT
    MinTemperatureF
FROM
    weather
WHERE
    Events LIKE "Rain" AND
    ZIP = 94301