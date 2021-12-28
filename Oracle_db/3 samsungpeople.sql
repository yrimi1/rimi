--------self join 하나의 테이블로 두개의 테이블효과 
--drop TABLE samsung;
--delete from samsung;

CREATE TABLE samsung (
    id  int Primary Key,
    name    VARCHAR2(30),
    boss_id    INT
);

select * from samsung;

insert into samsung values (1, '이건희', 1);
insert into samsung values (2, '홍라희', 2);
insert into samsung values (3, '이부진', 1);
insert into samsung values (4, '이재용', 1);
insert into samsung values (5, '신라호텔', 3);
insert into samsung values (6, '산성전자' ,4);
insert into samsung values (7, '수원삼성', 4);
insert into samsung values (8, '삼성라이온즈', 4);


--self join  을 하려면 테이블에 이름을 붙여야 한다.
select aa.name boss, bb.name name
from samsung aa join samsung bb on aa.id=bb.boss_id;

