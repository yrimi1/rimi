--그룹별로 묶기 
select * from book order by publisher;


--출판사별 가격
select sum(price), publisher from book GROUP by publisher;

--출판사당 책의 수
--count(*): group by 로 나눴을때 같은 그룹으로 묶이는것의 개수
select count(*), publisher from book GROUP by publisher ORDER by count(*) desc;

--책들의 가격 총합
select sum(price)총가격 from book;

--그룹바이 한상태로 조건절 추가하고싶다면 해빙써야한다
--책이 2권 이상인 출판사만 출력
select publisher from book GROUP BY publisher HAVING count(*)>1;


select * from book;
select max(price)from book;

select * from book where price = (select max(price)from book);
select * from book where price = (select min(price)from book);