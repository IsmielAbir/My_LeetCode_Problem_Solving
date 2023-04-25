select E1.name from Employee as E1 join Employee as E2
on E1.id = E2.managerId
group by E1.id, E1.name
having count(E2.id)>=5