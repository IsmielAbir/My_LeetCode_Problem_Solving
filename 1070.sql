
select a.product_id, a.year as first_year, a.quantity, a.price
from Sales as a inner join  
(select product_id, min(year) as year from Sales group by product_id) as b
on a.year = b.year and a.product_id = b.product_id
