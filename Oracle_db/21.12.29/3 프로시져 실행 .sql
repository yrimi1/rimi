exec add_person(4,'김민아','111-2222-3333')
exec add_person(5,'윤혜림','000-111-2222');
select * from simple_address_book;


exec delete_person(1);
select * from simple_address_book;


exec UPDATE_person(2,'권도균');
SELECT * FROM simple_address_book;

var o_cursor refcursor;
exec person_select('이동준', : o_cursor) 
print o_cursor; 

--var o_cursor refcursor; -- o_cursor 변수선언
--exec person_select('이동준', : o_cursor) --o_cursor 에 저장 
--print o_cursor; -- o_cursor에 있는 것을 print


--exec add_person(10,'이동준','010-1111-9999');
--exec add_person(7,'이동준','010-2222-9999');