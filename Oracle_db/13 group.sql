--�׷캰�� ���� 
select * from book order by publisher;


--���ǻ纰 ����
select sum(price), publisher from book GROUP by publisher;

--���ǻ�� å�� ��
--count(*): group by �� �������� ���� �׷����� ���̴°��� ����
select count(*), publisher from book GROUP by publisher ORDER by count(*) desc;

--å���� ���� ����
select sum(price)�Ѱ��� from book;

--�׷���� �ѻ��·� ������ �߰��ϰ�ʹٸ� �غ�����Ѵ�
--å�� 2�� �̻��� ���ǻ縸 ���
select publisher from book GROUP BY publisher HAVING count(*)>1;


select * from book;
select max(price)from book;

select * from book where price = (select max(price)from book);
select * from book where price = (select min(price)from book);