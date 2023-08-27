# Write your MySQL query statement below
select p.product_id, round(sum(p.price*u.units)/sum(u.units),2) as average_price
from prices p left join unitsSold u
on p.product_id = u.product_id
AND u.purchase_date between p.start_date AND p.end_date
group by p.product_id