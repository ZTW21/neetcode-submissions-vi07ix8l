-- Write your query below
-- select customer_id, customer_name
-- from customers
-- where (select customer ) 

select c.customer_id, c.customer_name
from customers c
where c.customer_id in (
    select customer_id from orders where product_name = 'A'
) and c.customer_id in (
    select customer_id from orders where product_name = 'B'
) and c.customer_id not in (
    select customer_id from orders where product_name = 'C'
)
ORDER BY c.customer_name;