select v.customer_id, count(v.visit_id) as count_no_trans 
from visits v left join Transactions e
on v.visit_id = e.visit_id
WHERE e.transaction_id IS NULL 
GROUP BY v.customer_id; 