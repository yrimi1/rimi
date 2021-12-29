--drop TABLE singer;
--drop TABLE song;

-- song �� �θ� ���̺�... ���� �����,  
--singer�� �ڽ����̺�... ���⿡��singer���̺��� hit_song_id�� song ���̺��� id�� �����Ұ���.
-- foreign key ���鋚�� Ÿ�Կ� ���� (hit_song_id  == id �� Ÿ���� int �� ����)

CREATE TABLE song (
    id    INT PRIMARY KEY,
    title VARCHAR2(40) NOT NULL,
    price INT
);


CREATE TABLE singer (
    id int Primary key,
    name    VARCHAR2(30) NOT NULL,
    hit_song_id     INT,
    FOREIGN key (hit_song_id) references song(id)
);

--��Ʈ���� ���� ���̵� �����Ұ���. Ÿ�Կ� ���� 
--�뷡���� �ֱ� 


SELECT * FROM song;
SELECT * FROM singer;

insert into song values(1, '�Ѹ�', 10000);
insert into song values(2, 'gee', 9000);
insert into song values(3, 'next lavel', 8000);

insert into singer values(1, '�극�̺�ɽ�', null);
insert into singer values(2, 'new�극�̺�ɽ�', 1);
insert into singer values(3, '�ҳ�ô�', 2);
insert into singer values(4, '�̵���', null);



------���� �غ��ž� ------------
--ansi SQL

--��Ʈ���� �����ϴ� ������ ��� 
select name, title from singer join song on singer.hit_song_id = song.id;

--left join
select name, title from singer left join song on singer.hit_song_id = song.id;

--right join
select name, title from singer right join song on singer.hit_song_id = song.id;

--full join(=outer join ) left right ��ģ��.... ��Ʈ�� ���� ����, �������� �뷡 ��� ���
select name, title from singer full join song on singer.hit_song_id = song.id;


