--drop TABLE singer;
--drop TABLE song;

-- song 이 부모 테이블... 먼저 만들것,  
--singer가 자식테이블... 여기에서singer테이블의 hit_song_id이 song 테이블의 id를 참조할것임.
-- foreign key 만들떄는 타입에 주의 (hit_song_id  == id 의 타입이 int 로 동일)

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

--히트송이 송의 아이디를 참조할것임. 타입에 주의 
--노래부터 넣기 


SELECT * FROM song;
SELECT * FROM singer;

insert into song values(1, '롤린', 10000);
insert into song values(2, 'gee', 9000);
insert into song values(3, 'next lavel', 8000);

insert into singer values(1, '브레이브걸스', null);
insert into singer values(2, 'new브레이브걸스', 1);
insert into singer values(3, '소녀시대', 2);
insert into singer values(4, '이동준', null);



------조인 해볼거양 ------------
--ansi SQL

--히트송이 존재하는 가수만 출력 
select name, title from singer join song on singer.hit_song_id = song.id;

--left join
select name, title from singer left join song on singer.hit_song_id = song.id;

--right join
select name, title from singer right join song on singer.hit_song_id = song.id;

--full join(=outer join ) left right 합친것.... 히트송 없는 가수, 가수없는 노래 모두 출력
select name, title from singer full join song on singer.hit_song_id = song.id;


