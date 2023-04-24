select C.name as Customers 
from Customers as C left join Orders as O
on C.id = O.customerId 
where o.customerId is null