select if(id%2!=0, if(id = (select max(id) from seat), id, id+1), id-1) as id, student
from seat
order by id