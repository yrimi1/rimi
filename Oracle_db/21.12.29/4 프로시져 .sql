--procedure ���ν��� (�Լ�)

--���ν����� ���� insert,up
select * from simple_address_book;

create or replace procedure add_person
(
    mynum in int, --�Ű�����, in Ű����� �Ű������� �ǹ���
    myname varchar2,
    mypn varchar2
)
IS
BEGIN
    insert into simple_address_book values(mynum, myname, mypn);
END add_person;
-- ���ν����� �������ϰ� ���� , �׽�Ʈ �ϰ� �ʹٸ� �ݵ�� END �ڿ� / �߰� �Ұ�


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
    mynum      IN INT, --�̸��� �ٲ� �л��� ��ȣ
    changename IN VARCHAR2 -- ���� ������ ������ �̸�
)
IS
        tempvar VARCHAR2(20) := '�л�';
BEGIN
    tempvar := changeName  || tempvar ; -- ���� �ٲ��̸� + �л� ex)�̵����л�
    update simple_address_book set name = tempvar
    where num = mynum;
END update_person;

--------------------------------------------------------------------------------------------
--select procedure �� cursor�� ��ȯ ���ش�.
-- �׸��� �� cursor�� �̿��ؼ� ����� ���

CREATE PROCEDURE person_select
(
    myname in varchar2, --�Ű����� 
    o_cursor out sys_refcursor -- Ŀ����ȯ
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

