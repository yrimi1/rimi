CREATE TABLE mykbmajor
(
    name    VARCHAR2(30) NOT NULL,
    code    CHAR(3) PRIMARY KEY,
    regdate TIMESTAMP DEFAULT sysdate
);
insert into mykbmajor (name,code) values ('정보기술개발','001');
select *from mykbmajor;



CREATE TABLE mykbstudent (
    name        VARCHAR2(30),
    age         INT,
    hakbeon     CHAR(10),
    hakgwa_code CHAR(3),
    regdate     TIMESTAMP DEFAULT sysdate
);

--외래키 설정을 추가하는법
ALTER TABLE mykbstudent ADD CONSTRAINT fk_mykbstu FOREIGN KEY(hakgwa_code) REFERENCES mykbmajor(code);

insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('이동준',33,'123A','001');
insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('이종준',33,'123B','555');

INSERT into mykbmajor (name,code) values ('전자과','002');

insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('이종준',33,'123B','002');
insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('이봉준',33,'123C','001');

SELECT * FROM mykbmajor;
SELECT * FROM mykbstudent;

---------------------------------------------------------
--이동준 123A 정보기술개발
--이동준 123A 정보기술개발
--이동준 123A 정보기술개발


--mykbstudent - > a로 치환
--mykbmajor - > b로 치환

select a.name,hakbeon, b.name from mykbstudent a join mykbmajor b on a.hakgwa_code = b.code;

select a.name,hakbeon, b.name from mykbstudent a join mykbmajor b on a.hakgwa_code = b.code where b.code = '001';
select a.name,hakbeon, b.name from mykbstudent a join mykbmajor b on a.hakgwa_code = b.code where b.name = '정보기술개발';

