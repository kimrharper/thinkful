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
	available = 'f'
ORDER BY
	months ASC)

select
count(price) total
from
month_prices
group by months
