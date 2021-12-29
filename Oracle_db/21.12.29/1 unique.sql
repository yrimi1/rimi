select * from orders; 
select * from customer;
select * from book;

--primary key
--unique 겹치면 안되는데 null값가능
--예) 전화번호
CREATE TABLE simple_address_book (
    num          INT PRIMARY KEY,
    name         VARCHAR2(30) NOT NULL,
    phone_number VARCHAR2(20) UNIQUE
);

select * from simple_address_book;

insert into simple_address_book values ( 1, '이동준', null);  --ok
insert into simple_address_book values ( 2, '권도균', '010-xxxx-zzzz'); --ok
insert into simple_address_book values ( 3, '이동준', '010-2940-1613'); --ok
--insert into simple_address_book values ( 4, '이강호', '010-2940-1613'); --fail (전화번호 중복)
--insert into simple_address_book values ( 5, null, null);  -- 이름없어서 fail
--insert into simple_address_book values ( 6, null, 'xxx-xxxx-xxxx'); - 이름없어서 fail

--booname을 bookname로 변경한다.
--alter table book rename column booname to bookname;

select * from orders;
select * from book;

--주문번호 책이름 가격 (책이름만 나온다)
select orderid, book.bookname, orders.saleprice, orders.custid from 
orders join book on orders.bookid = book.bookid;

--주문번호, 고객명 , saleprice , bookid (고객 이름만 나온다)
select orderid, customer. name, saleprice, bookid from 
orders join customer on orders. custid = customer.custid;

--중첩질의 를 통해 order테이블의 고객명 과 책이름을 모두 출력하게 하기
-- 1번 방법 (중첩질의안쓰고...)
select orders.orderid , book.bookname ,orders.saleprice ,orders.custid ,customer.name   
FROM  orders, book, customer  
where orders.custid = customer.custid and orders.bookid=book.bookid
order by orderid;

--2번 방법(중첩질의 사용)
-- order와 book  + custom
select orderid, aa.bookname, customer.name, saleprice from 
(select orderid, book.bookname, orders.saleprice, orders.custid from 
orders join book on orders.bookid=book.bookid) aa join customer on 
aa.custid = customer.custid order by orderid;

--book 과 (orders와 customer를 join한 테이블)의 join
select orderid, aa.name, book.bookname, saleprice from 
(select orderid, customer. name, saleprice, bookid from 
orders join customer on orders. custid = customer.custid) aa join book on 
aa.bookid = book.bookid order by orderid;


--위 코드의 select 괄호문 은 가상의 테이블... 이것을 더 심플하게..
--view라는 가상 테이블을 사용하기
-- view
-- 가상테이블
-- 실제 존재하는 건 아닌 데,
-- 복잡한 쿼리문에 들어갈 select 결과물을 미리 만들어 두기

create or replace view mytestview as 
select * from orders;
select * from mytestview; -- select * from orders라는 결과를 뷰로 만듦
--or replace는 생략 가능
--이걸 써주는 이유는 이름이 겹치는 view를 만들게 되면 새걸로 덮어쓰기 위함
-- 새걸로 덮어쓸 생각이 없다면 or replace 생략가능
create view expensive_book as 
select * from book where price>10000; -- book테이블에서 만원넘는 책들만 뷰로 만듦

select * from expensive_book; -- 10000원을 넘는 책만 출력됨



-- 뷰 사용해서 간단하게 만들기 
select orderid, aa.bookname, customer.name, saleprice from 
aa join customer on 
aa.custid = customer.custid order by orderid;

create view aa as select orderid, book.bookname, orders.saleprice, orders.custid from 
orders join book on orders.bookid=book.bookid;



