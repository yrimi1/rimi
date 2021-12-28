CREATE TABLE mydbhakgwa
(
    code CHAR(3) PRIMARY KEY,
    NAME VARCHAR2(30) 
);

CREATE TABLE mydbstudent
(
    hakbeon VARCHAR2(10) PRIMARY KEY,
    NAME VARCHAR2(60),
    age INT,
    hakgwacode CHAR(3),  FOREIGN KEY(hakgwacode) REFERENCES mydbhakgwa(code)
);

INSERT INTO mydbhakgwa VALUES ('001', '컴공');
INSERT INTO mydbhakgwa VALUES ('002', '아동가족학');

-- 학생을 추가하려고 한다. 현재는 컴공과 아동가족학과학생만 넣을수있다.

insert into mydbstudent values('12345A','이동준',33,'001');
insert into mydbstudent values('12345B','류경문',23,'001');
insert into mydbstudent values('12345C','윤혜림',20,'002');
insert into mydbstudent values('12345D','장상은',25,'002');
insert into mydbstudent values('12345E','구혜진',27,'002');

SELECT * FROM mydbhakgwa;
SELECT * FROM mydbstudent;
