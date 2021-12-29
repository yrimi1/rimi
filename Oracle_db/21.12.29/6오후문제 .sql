--drop table userTBI;
--drop table buyTBI;

create table userTBI
( 
    userid CHAR(8) PRIMARY KEY,
    username VARCHAR2(10) not null
);

insert into userTBI values ('KHD' , '��ȣ��');
insert into userTBI values ('KJD' , '������');
insert into userTBI values ('KKJ' , '�豹��');
insert into userTBI values ('KYM' , '��븸');
insert into userTBI values ('LHJ' , '������');
insert into userTBI values ('LKK' , '�̰��');
insert into userTBI values ('NHS' , '����');
insert into userTBI values ('PSH' , '�ڼ�ȫ');
insert into userTBI values ('SDY' , '�ŵ���');
insert into userTBI values ('YJS' , '���缮');

----------------------------------------------------------------------------

create table buyTBI
( 
    num int PRIMARY key,
    userid char(8) ,  foreign key (userid) references userTBI(userid),
    prodName char(20) not null,
    price int not null,
    Amount int not null
);

create sequence sq_1 start with 1 increment by 1 maxvalue 100
cycle nocache;

insert into buyTBI values (sq_1.nextval, 'KHD','�ȭ',30,2);
insert into buyTBI values (sq_1.nextval, 'KHD','��Ʈ��',1000,1);
insert into buyTBI values (sq_1.nextval, 'KYM','�����',200,1);
insert into buyTBI values (sq_1.nextval, 'PSH','�����',200,5);
insert into buyTBI values (sq_1.nextval, 'KHD','û����',50,3);
insert into buyTBI values (sq_1.nextval, 'PSH','�޸�',80,10);
insert into buyTBI values (sq_1.nextval, 'KJD','å',15,5);
insert into buyTBI values (sq_1.nextval, 'LHJ','å',15,2);
insert into buyTBI values (sq_1.nextval, 'LHJ','û����',50,1);
insert into buyTBI values (sq_1.nextval, 'PSH','�ȭ',30,2);
insert into buyTBI values (sq_1.nextval, 'LHJ','å',15,1);
insert into buyTBI values (sq_1.nextval, 'PSH','�ȭ',30,2);

SELECT * FROM userTBI;
SELECT * FROM buyTBI;

-- alter table ���̺�� remane column ��Ÿ to  ���ľ���



--1. ������ ���ݰ� ���� �̿��ؼ� �� ����ڰ� �� ���Ǵ� �� ����� ����Ͻÿ�.
--(select * from buyTBI where price * Amount)
select username, prodName, price,Amount, (price * Amount) from userTBI join buyTBI on buyTBI.userid = userTBI.userid;

select username as "����ڸ�" , prodName as "��ǰ��", price as "����" ,Amount as "����" ,(price * Amount) as "�հ�" 
from userTBI join buyTBI on buyTBI.userid = userTBI.userid;


--2. ����ں� �ѱ��ž��� ���Ͻÿ�..
--�����̸����� �׷���� �� ������ ��� ���� �ϹǷ� �÷��� 2���� ����.
select username, sum(price * Amount) from userTBI join buyTBI on buyTBI.userid = userTBI.userid GROUP by usermane;



--3. �� ���ž��� 1000���� �Ѵ� ����鸸 ����Ͻÿ�.

--4. �� ���ž��� ���� ���� ����� ���� ����� �̸��� ������ ���� ����Ͻÿ�.