--1. Employee 테이블 생성
--사번, 이름, 나이, 직급 
--(자료형, 길이, pk 알아서 지정)
--drop TABLE Employee;

CREATE TABLE employee (
    sabeon  NUMBER PRIMARY KEY,
    name    VARCHAR2(20) NOT NULL,
    age     INT,
    jikgeup VARCHAR2(30)
);

--2. 최소 5명 이상의 데이터 입력하기
--예시)  2009038033 'lee' 33 'senior'
--         2021000111 'park' 19 'manager'
--         2021000112 'kim' 77 'beginner'
--         2021000113 'choi' 55 'senior'
--         2021000114 'Jang' 47 'manager'
insert into Employee values(2009038033, 'lee', 33, 'senior');
insert into Employee (sabeon,name,age,jikgeup) values(2021000111, 'park', 19,'manager');
insert into Employee (sabeon,name) values(2021000112, 'kim');
UPDATE employee set age = 77, jikgeup='beginner' where sabeon='2021000112';

insert into Employee values(2021000113, 'choi', 55, 'senior');
insert into Employee values(2021000114, 'Jang', 47, 'manager');


--3. 나이가 30살 이하인 사람의 직급을  'beginner'로 지정하기
update Employee set jikgeup ='beginner' where age<=30;

--4. 나이가 50살 이상인 사람의 직급을 'manager'로 지정하기
update Employee set jikgeup ='manager' where age>=50;


--5. 나이가 70살 이상인 사람은 삭제하기
delete from Employee where age>70;

--6. 모두 조회해보기
select * from Employee;
select * from Employee order by age;


--7. 직급이 senior인 사람 조회해보기
select * from Employee where jikgeup ='senior';
select sabeon , age from Employee where jikgeup ='senior';

--컬럼명 변경!!!!!!
select sabeon as "사원번호" , age as "나이" from employee;

--이름에 a 라는 글자가 있는 사람만 조회하기
select * from employee where name like '%a%'; 

commit;