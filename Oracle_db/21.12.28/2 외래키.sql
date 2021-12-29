select * from hakgwa;
select * from student;

select hakgwa. name 학과명, hakbeon 학번, student. name 이름
from hakgwa, student where 
hakgwa.code=student.hakgwa_code;

------------------------------------------------------------------------------
