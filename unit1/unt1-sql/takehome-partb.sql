with
spenders
as(
select
	customers.state,
	transactions.customer_id,
	sum(transactions.transact_amt) as sum_total
from
	transactions
join
	customers
on
	transactions.customer_id = customers.customer_id
group by
	transactions.customer_id
order by
	sum_total desc)

select
	*
from
	spenders
group by
	state,customer_id
	
