# 튜플(tuple)-------------------------------------
#리스트 와 다르게 변경이나 추가불가 , 속도가더 빠름 변경되지않는 목록을 사용할때 튜플사용
# 튜플은 릴레이션을 구성하는 각각의 행,, 튜플의 수를 카디널리티(Cardinality) 또는 기수
menu = ("돈까스","치즈까쓰") #튜플선언
print(menu[0])
print(menu[1])

#menu.add("생선까스") 튜플은 변경x,추가안됨

#변수 각자선언 후 출력
name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)

#튜플로 한번에 변수선언
(name,age,hobby) = ("김종국",20,"코딩")
print(name,age,hobby)


# 튜플의 선언
apsb =  ("아메리카노","라떼","모카","더이상 뭘 넣지")
print(apsb)

a,b,c,d,e,f,g=('aa','bb','cc','dd','ee','ff','gg')
print(a,b,c,d,e,f,g)

 #### 대괄호로 묶으면 리스트 , 소괄호로 묶으면 튜플 ####