select Person.firstName, Person.lastName, Address.city, Address.state 
from Person LEFT JOIN Address
on Person.personId = Address.personId