# Write your MySQL query statement below
select u.name, COALESCE(SUM(r.distance), 0) as travelled_distance
from users u left join rides r
on u.id = r.user_id
group by u.id, u.name
order by travelled_distance desc, u.name asc