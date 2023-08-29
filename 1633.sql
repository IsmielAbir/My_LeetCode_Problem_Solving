select r.contest_id, round(count(contest_id)*100/(select count(*) from users),2) as percentage
from users u join register r
on u.user_id = r.user_id
group by contest_id
order by percentage desc, contest_id