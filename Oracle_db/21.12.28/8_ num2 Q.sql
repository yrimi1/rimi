CREATE TABLE mykbmajor
(
    name    VARCHAR2(30) NOT NULL,
    code    CHAR(3) PRIMARY KEY,
    regdate TIMESTAMP DEFAULT sysdate
);
insert into mykbmajor (name,code) values ('�����������','001');
select *from mykbmajor;



CREATE TABLE mykbstudent (
    name        VARCHAR2(30),
    age         INT,
    hakbeon     CHAR(10),
    hakgwa_code CHAR(3),
    regdate     TIMESTAMP DEFAULT sysdate
);

--�ܷ�Ű ������ �߰��ϴ¹�
ALTER TABLE mykbstudent ADD CONSTRAINT fk_mykbstu FOREIGN KEY(hakgwa_code) REFERENCES mykbmajor(code);

insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('�̵���',33,'123A','001');
insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('������',33,'123B','555');

INSERT into mykbmajor (name,code) values ('���ڰ�','002');

insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('������',33,'123B','002');
insert into mykbstudent (name,age,hakbeon,hakgwa_code) values ('�̺���',33,'123C','001');

SELECT * FROM mykbmajor;
SELECT * FROM mykbstudent;

---------------------------------------------------------
--�̵��� 123A �����������
--�̵��� 123A �����������
--�̵��� 123A �����������


--mykbstudent - > a�� ġȯ
--mykbmajor - > b�� ġȯ

select a.name,hakbeon, b.name from mykbstudent a join mykbmajor b on a.hakgwa_code = b.code;

select a.name,hakbeon, b.name from mykbstudent a join mykbmajor b on a.hakgwa_code = b.code where b.code = '001';
select a.name,hakbeon, b.name from mykbstudent a join mykbmajor b on a.hakgwa_code = b.code where b.name = '�����������';

