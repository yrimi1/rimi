select *from mystudent;
SELECT * FROM mystudent where age>20;
SELECT * FROM mystudent where age>20 and age<30;
SELECT * FROM mystudent where name = '���湮' or name='�ǵ���';
select * from mystudent where name='��'||'�湮';

select * from mystudent order by age; --��������
select * from mystudent order by age desc; --��������

--name �� �� �ձ��ڴ� ���̰� , �� �ڿ� ���� ���� �������
select * from mystudent where name like '��%'; --���� �Ǿ��� ��� ���

--�̸��� ���� ��������� �ִٰ� ġ��..

insert into mystudent values('���±�',40,'12345');
SELECT * FROM mystudent where name like '%��'

