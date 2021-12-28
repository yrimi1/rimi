--1. Employee ���̺� ����
--���, �̸�, ����, ���� 
--(�ڷ���, ����, pk �˾Ƽ� ����)
--drop TABLE Employee;

CREATE TABLE employee (
    sabeon  NUMBER PRIMARY KEY,
    name    VARCHAR2(20) NOT NULL,
    age     INT,
    jikgeup VARCHAR2(30)
);

--2. �ּ� 5�� �̻��� ������ �Է��ϱ�
--����)  2009038033 'lee' 33 'senior'
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


--3. ���̰� 30�� ������ ����� ������  'beginner'�� �����ϱ�
update Employee set jikgeup ='beginner' where age<=30;

--4. ���̰� 50�� �̻��� ����� ������ 'manager'�� �����ϱ�
update Employee set jikgeup ='manager' where age>=50;


--5. ���̰� 70�� �̻��� ����� �����ϱ�
delete from Employee where age>70;

--6. ��� ��ȸ�غ���
select * from Employee;
select * from Employee order by age;


--7. ������ senior�� ��� ��ȸ�غ���
select * from Employee where jikgeup ='senior';
select sabeon , age from Employee where jikgeup ='senior';

--�÷��� ����!!!!!!
select sabeon as "�����ȣ" , age as "����" from employee;

--�̸��� a ��� ���ڰ� �ִ� ����� ��ȸ�ϱ�
select * from employee where name like '%a%'; 

commit;