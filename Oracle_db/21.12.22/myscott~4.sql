select *from mystudent;
SELECT * FROM mystudent where age>20;
SELECT * FROM mystudent where age>20 and age<30;
SELECT * FROM mystudent where name = '류경문' or name='권도균';
select * from mystudent where name='류'||'경문';

select * from mystudent order by age; --오름차순
select * from mystudent order by age desc; --내림차순

--name 의 맨 앞글자는 권이고 , 그 뒤엔 뭐가 들어가도 상관없음
select * from mystudent where name like '권%'; --성이 권씨인 사람 출력

--이름의 끝이 같은사람이 있다고 치자..

insert into mystudent values('김태균',40,'12345');
SELECT * FROM mystudent where name like '%균'

