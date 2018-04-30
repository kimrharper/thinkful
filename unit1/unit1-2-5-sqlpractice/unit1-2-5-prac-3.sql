WITH month_prices
AS
(SELECT
	listing_id,
	date,
	CAST(REPLACE(price, '$', ' ') as float) price,
	strftime('%m', calendar.date) months
FROM
	calendar
WHERE
	available = 't'
ORDER BY
	months ASC)




select
avg(price)
from
month_prices
group by months


	--select distinct * from month_prices

/*
WITH month_prices
AS
(SELECT
	*,
	listings.price,
	strftime('%m', calendar.date) months
FROM
	calendar
JOIN
	listings
ON
	calendar.listing_id = listings.id
ORDER BY
	months ASC)


select
	*
from month_prices
	

SELECT
	months,
	count(price),
	sum(price),
	(sum(price)/count(price)),
	avg(price)
FROM
	month_prices
--where months in ('01', '02', '03')
GROUP BY months
*/