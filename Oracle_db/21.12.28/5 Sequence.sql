--Sequence 
--������ ���� �� Ȥ�� ���̺��� �����ϱ� ���� 
--���� �������� �����

create sequence myseq start with 1 increment by 1 maxvalue 100
cycle nocache;


insert into simpletable values (myseq.nextval, '�̵���');
insert into simpletable values (myseq.nextval, '�ǿ��');
insert into simpletable values (myseq.nextval, '�̿���');

select * from simpletable;

