with
gmail
as
(select
customers.customer_id
from
customers
where customers.email like '%gmail%')

select products.product_name
from
(select
	transactions.product_id as product,
	count(transactions.product_id) as total_p
from
	gmail
join
	transactions
on
	transactions.customer_id = gmail.customer_id
WHERE transactions.transact_at BETWEEN datetime('now', '-1 month') AND datetime('now', 'localtime')
group by
	product
order by
total_p desc
limit 5) g_product

join
	products
on
	g_product.product = products.product_id