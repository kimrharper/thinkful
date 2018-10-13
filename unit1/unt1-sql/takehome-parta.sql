/* popularity determined by attempted purchase count */

with 
	states
as (
select
	customers.state,
	count(transactions.product_id) as product_count,
	transactions.product_id
from
	customers
join
	transactions
on
	customers.customer_id = transactions.customer_id
group by
	transactions.product_id)
	
select
	t_total.state,
	t_total.product_name
from(
select
	s.state,
	max(s.product_count),
	p.product_name
from
	states as s
join
	products as p
on
	s.product_id = p.product_id

group by
	state) t_total
	