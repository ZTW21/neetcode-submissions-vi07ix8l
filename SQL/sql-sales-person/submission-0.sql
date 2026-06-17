-- Write your query below
SELECT sales_person.name
FROM sales_person
WHERE sales_person.sales_id NOT IN (
    SELECT orders.sales_id
    FROM orders
    JOIN company on orders.com_id = company.com_id
    WHERE company.name = 'CRIMSON'
);
