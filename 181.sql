select E.name as Employee
from Employee as E inner join employee as M 
on E.managerId = M.id
where E.Salary > M.Salary
