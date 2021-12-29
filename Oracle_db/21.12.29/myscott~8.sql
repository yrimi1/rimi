create table Univ_student
( 
    userid CHAR(8) PRIMARY KEY,
    username VARCHAR2(10)
);

create table Univ_major
( 
    userid CHAR(8) PRIMARY KEY,
    username VARCHAR2(10) not null
);
