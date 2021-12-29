select * from orders; 
select * from customer;
select * from book;

--primary key
--unique ��ġ�� �ȵǴµ� null������
--��) ��ȭ��ȣ
CREATE TABLE simple_address_book (
    num          INT PRIMARY KEY,
    name         VARCHAR2(30) NOT NULL,
    phone_number VARCHAR2(20) UNIQUE
);

select * from simple_address_book;

insert into simple_address_book values ( 1, '�̵���', null);  --ok
insert into simple_address_book values ( 2, '�ǵ���', '010-xxxx-zzzz'); --ok
insert into simple_address_book values ( 3, '�̵���', '010-2940-1613'); --ok
--insert into simple_address_book values ( 4, '�̰�ȣ', '010-2940-1613'); --fail (��ȭ��ȣ �ߺ�)
--insert into simple_address_book values ( 5, null, null);  -- �̸���� fail
--insert into simple_address_book values ( 6, null, 'xxx-xxxx-xxxx'); - �̸���� fail

--booname�� bookname�� �����Ѵ�.
--alter table book rename column booname to bookname;

select * from orders;
select * from book;

--�ֹ���ȣ å�̸� ���� (å�̸��� ���´�)
select orderid, book.bookname, orders.saleprice, orders.custid from 
orders join book on orders.bookid = book.bookid;

--�ֹ���ȣ, ���� , saleprice , bookid (�� �̸��� ���´�)
select orderid, customer. name, saleprice, bookid from 
orders join customer on orders. custid = customer.custid;

--��ø���� �� ���� order���̺��� ���� �� å�̸��� ��� ����ϰ� �ϱ�
-- 1�� ��� (��ø���ǾȾ���...)
select orders.orderid , book.bookname ,orders.saleprice ,orders.custid ,customer.name   
FROM  orders, book, customer  
where orders.custid = customer.custid and orders.bookid=book.bookid
order by orderid;

--2�� ���(��ø���� ���)
-- order�� book  + custom
select orderid, aa.bookname, customer.name, saleprice from 
(select orderid, book.bookname, orders.saleprice, orders.custid from 
orders join book on orders.bookid=book.bookid) aa join customer on 
aa.custid = customer.custid order by orderid;

--book �� (orders�� customer�� join�� ���̺�)�� join
select orderid, aa.name, book.bookname, saleprice from 
(select orderid, customer. name, saleprice, bookid from 
orders join customer on orders. custid = customer.custid) aa join book on 
aa.bookid = book.bookid order by orderid;


--�� �ڵ��� select ��ȣ�� �� ������ ���̺�... �̰��� �� �����ϰ�..
--view��� ���� ���̺��� ����ϱ�
-- view
-- �������̺�
-- ���� �����ϴ� �� �ƴ� ��,
-- ������ �������� �� select ������� �̸� ����� �α�

create or replace view mytestview as 
select * from orders;
select * from mytestview; -- select * from orders��� ����� ��� ����
--or replace�� ���� ����
--�̰� ���ִ� ������ �̸��� ��ġ�� view�� ����� �Ǹ� ���ɷ� ����� ����
-- ���ɷ� ��� ������ ���ٸ� or replace ��������
create view expensive_book as 
select * from book where price>10000; -- book���̺��� �����Ѵ� å�鸸 ��� ����

select * from expensive_book; -- 10000���� �Ѵ� å�� ��µ�



-- �� ����ؼ� �����ϰ� ����� 
select orderid, aa.bookname, customer.name, saleprice from 
aa join customer on 
aa.custid = customer.custid order by orderid;

create view aa as select orderid, book.bookname, orders.saleprice, orders.custid from 
orders join book on orders.bookid=book.bookid;



