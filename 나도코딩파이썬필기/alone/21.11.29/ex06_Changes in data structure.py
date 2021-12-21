##자료 구조의 변경---------------------------
menu = {"아메리카노","라떼","모카"}
print(menu,type(menu)) #{class 'set'} 세트 형식으로 선언했기떄문제 이렇게 나온다.

menu = list(menu)
print(menu,type(menu)) #[class 'list']

menu = tuple(menu)
print(menu,type(menu))  #(class 'tuple')

menu = set(menu)
print(menu,type(menu))