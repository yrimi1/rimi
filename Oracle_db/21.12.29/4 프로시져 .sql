--procedure 프로시져 (함수)

--프로시져를 통한 insert,up
select * from simple_address_book;

create or replace procedure add_person
(
    mynum in int, --매개변수, in 키워드는 매개변수를 의미함
    myname varchar2,
    mypn varchar2
)
IS
BEGIN
    insert into simple_address_book values(mynum, myname, mypn);
END add_person;
-- 프로시져를 컴파일하고 나서 , 테스트 하고 싶다면 반드시 END 뒤에 / 추가 할것


-------------------------------------------------------------------------------------------
create or replace  procedure delete_person
(
mynum in int
)
IS
BEGIN
    delete from simple_address_book where num = mynum;
END delete_person;

-------------------------------------------------------------------------------------------
create /*or replace*/ PROCEDURE update_person (
    mynum      IN INT, --이름을 바꿀 학생의 번호
    changename IN VARCHAR2 -- 내가 실제로 적용할 이름
)
IS
        tempvar VARCHAR2(20) := '학생';
BEGIN
    tempvar := changeName  || tempvar ; -- 내가 바꿀이름 + 학생 ex)이동준학생
    update simple_address_book set name = tempvar
    where num = mynum;
END update_person;

--------------------------------------------------------------------------------------------
--select procedure 는 cursor를 반환 해준다.
-- 그리고 이 cursor를 이용해서 결과를 출력

CREATE PROCEDURE person_select
(
    myname in varchar2, --매개변수 
    o_cursor out sys_refcursor -- 커서반환
)
IS
BEGIN
     OPEN o_cursor
     for
        select num, name,phone_number from simple_address_book
        where name = myname;
EXCEPTION
    when others then
    dbms_output.put_line('sql error : ' || SQLERRM);
    END person_select;
    
--DROP PROCEDURE person_select;

