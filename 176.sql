select ifNull(
  (select distinct salary as SecondHighestSalary
from Employee 
order by Salary desc
limit 1 offset 1), null
) as SecondHighestSalary