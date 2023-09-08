select p.product_id, p.product_name
from product p left join sales s
on p.product_id = s.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date)>= '2019-01-01' AND MAX(s.sale_date)<='2019-03-31';