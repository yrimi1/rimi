exec add_person(4,'��ξ�','111-2222-3333')
exec add_person(5,'������','000-111-2222');
select * from simple_address_book;


exec delete_person(1);
select * from simple_address_book;


exec UPDATE_person(2,'�ǵ���');
SELECT * FROM simple_address_book;

var o_cursor refcursor;
exec person_select('�̵���', : o_cursor) 
print o_cursor; 

--var o_cursor refcursor; -- o_cursor ��������
--exec person_select('�̵���', : o_cursor) --o_cursor �� ���� 
--print o_cursor; -- o_cursor�� �ִ� ���� print


--exec add_person(10,'�̵���','010-1111-9999');
--exec add_person(7,'�̵���','010-2222-9999');