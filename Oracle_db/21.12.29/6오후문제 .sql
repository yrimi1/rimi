--drop table userTBI;
--drop table buyTBI;

create table userTBI
( 
    userid CHAR(8) PRIMARY KEY,
    username VARCHAR2(10) not null
);

insert into userTBI values ('KHD' , '강호동');
insert into userTBI values ('KJD' , '김제동');
insert into userTBI values ('KKJ' , '김국진');
insert into userTBI values ('KYM' , '김용만');
insert into userTBI values ('LHJ' , '이휘재');
insert into userTBI values ('LKK' , '이경규');
insert into userTBI values ('NHS' , '남희석');
insert into userTBI values ('PSH' , '박수홍');
insert into userTBI values ('SDY' , '신동엽');
insert into userTBI values ('YJS' , '유재석');

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

insert into buyTBI values (sq_1.nextval, 'KHD','운동화',30,2);
insert into buyTBI values (sq_1.nextval, 'KHD','노트북',1000,1);
insert into buyTBI values (sq_1.nextval, 'KYM','모니터',200,1);
insert into buyTBI values (sq_1.nextval, 'PSH','모니터',200,5);
insert into buyTBI values (sq_1.nextval, 'KHD','청바지',50,3);
insert into buyTBI values (sq_1.nextval, 'PSH','메모리',80,10);
insert into buyTBI values (sq_1.nextval, 'KJD','책',15,5);
insert into buyTBI values (sq_1.nextval, 'LHJ','책',15,2);
insert into buyTBI values (sq_1.nextval, 'LHJ','청바지',50,1);
insert into buyTBI values (sq_1.nextval, 'PSH','운동화',30,2);
insert into buyTBI values (sq_1.nextval, 'LHJ','책',15,1);
insert into buyTBI values (sq_1.nextval, 'PSH','운동화',30,2);

SELECT * FROM userTBI;
SELECT * FROM buyTBI;

-- alter table 테이블명 remane column 오타 to  고쳐쓰기



--1. 물건의 가격과 수량 이용해서 각 사용자가 각 물건당 얼마 썼는지 출력하시오.
--(select * from buyTBI where price * Amount)
select username, prodName, price,Amount, (price * Amount) from userTBI join buyTBI on buyTBI.userid = userTBI.userid;

select username as "사용자명" , prodName as "제품명", price as "가격" ,Amount as "수량" ,(price * Amount) as "합계" 
from userTBI join buyTBI on buyTBI.userid = userTBI.userid;


--2. 사용자별 총구매액을 구하시오..
--유저이름으로 그룹바이 한 다음에 계산 시작 하므로 컬럼을 2개만 쓸것.
select username, sum(price * Amount) from userTBI join buyTBI on buyTBI.userid = userTBI.userid GROUP by usermane;



--3. 총 구매액이 1000원이 넘는 사람들만 출력하시오.

--4. 총 구매액이 가장 높은 사람과 낮은 사람의 이름과 가격을 같이 출력하시오.