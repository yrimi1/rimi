drop TABLE singer;
drop TABLE song;


CREATE TABLE singer (
    id NUMBER Primary key,
    name    VARCHAR2(20) NOT NULL,
    age     INT
);

CREATE TABLE singer (
    sabeon  NUMBER PRIMARY KEY,
    name    VARCHAR2(20) NOT NULL,
    age     INT,
    jikgeup VARCHAR2(30)
);




SELECT * FROM singer;

insert into singer (id,name,hit_song_id) values(1, '브레이브걸스', 1000);
insert into singer (id,name,hit_song_id) values(2, '소녀시대', 2000);

insert into song (id,title,price) values(1,'롤린',10000);
insert into song (id,title,price) values(2,'gee',9000);
insert into song (id,title,price) values(3,'next lavel',8000);

