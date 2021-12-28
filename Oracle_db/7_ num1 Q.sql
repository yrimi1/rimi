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

INSERT INTO mydbhakgwa VALUES ('001', '�İ�');
INSERT INTO mydbhakgwa VALUES ('002', '�Ƶ�������');

-- �л��� �߰��Ϸ��� �Ѵ�. ����� �İ��� �Ƶ������а��л��� �������ִ�.

insert into mydbstudent values('12345A','�̵���',33,'001');
insert into mydbstudent values('12345B','���湮',23,'001');
insert into mydbstudent values('12345C','������',20,'002');
insert into mydbstudent values('12345D','�����',25,'002');
insert into mydbstudent values('12345E','������',27,'002');

SELECT * FROM mydbhakgwa;
SELECT * FROM mydbstudent;
