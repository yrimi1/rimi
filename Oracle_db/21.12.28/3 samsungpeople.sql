--------self join �ϳ��� ���̺�� �ΰ��� ���̺�ȿ�� 
--drop TABLE samsung;
--delete from samsung;

CREATE TABLE samsung (
    id  int Primary Key,
    name    VARCHAR2(30),
    boss_id    INT
);

select * from samsung;

insert into samsung values (1, '�̰���', 1);
insert into samsung values (2, 'ȫ����', 2);
insert into samsung values (3, '�̺���', 1);
insert into samsung values (4, '�����', 1);
insert into samsung values (5, '�Ŷ�ȣ��', 3);
insert into samsung values (6, '�꼺����' ,4);
insert into samsung values (7, '�����Ｚ', 4);
insert into samsung values (8, '�Ｚ���̿���', 4);


--self join  �� �Ϸ��� ���̺� �̸��� �ٿ��� �Ѵ�.
select aa.name boss, bb.name name
from samsung aa join samsung bb on aa.id=bb.boss_id;

