##리스트(list)------------------------------
# 리스트는 순서를 가지는 객체의 집합
# subway1 = 10 
# subway2 = 20 
# subway3 = 30

#원래는 이러게 변수를 설정해서 각자 저장
# 이걸 한번에 연속적인 공간에 묶어서 관리하게 하는 리스트 
# subway = [10,20,30] # 이렇게 쓴다 
# print(subway)

subway = ['유재석','조세호','박명수']
# print(subway1)
print(subway.index("조세호")) #조가타고있는 인덱스 번호 출력
subway.append('하하') # 리스트에 추가 (제일뒤)
subway.insert(1,'정형돈') #리스트에 추가 (끼워넣기)
print(subway)

#뒤어세부터 뺌
print(subway.pop())
print(subway)


