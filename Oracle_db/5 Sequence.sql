--Sequence 
--데이터 삽입 전 혹은 테이블을 생성하기 전에 
--먼저 시퀀스를 만든다

create sequence myseq start with 1 increment by 1 maxvalue 100
cycle nocache;


insert into simpletable values (myseq.nextval, '이동준');
insert into simpletable values (myseq.nextval, '권용규');
insert into simpletable values (myseq.nextval, '이원만');

select * from simpletable;

