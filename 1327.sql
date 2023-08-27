select p.product_name, sum(q.unit) as unit
from Products p left join Orders q
on p.product_id = q.product_id
where q.order_date between '2020-02-01' and '2020-02-29'
group by q.product_id
having unit>=100
order by q.product_id