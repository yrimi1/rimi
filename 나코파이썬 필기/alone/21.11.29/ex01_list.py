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
print("조세호의 인덱스 번호 : "+str(subway.index("조세호"))) #조가타고있는 인덱스 번호 출력
subway.append('하하') # 리스트에 추가 (제일뒤)
subway.insert(1,'정형돈') #리스트에 추가 (끼워넣기)
print("하하끝추가 형돈 중간추가한 리스트 : \n"+str(subway))


#한명씩 뒤에서부터 꺼냄
print(subway.pop()) #꺼내고 난 리스트가아니라 하나를 꺼내서 보여줌
print(subway)

# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)

#같은 이름의 사람이 몇명있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))


mylist = [5,2,4,3,1]
mylist.sort()  #정렬하기
print(mylist)
mylist.reverse()  #역순정렬
print(mylist)
mylist.clear() #리스트 모두 삭제
print(mylist)

#리스트에는 여러가지 자료형 섞어사용 가능
mixlist = ['조세호',20,True]
mylist2 = [1,3,5,3,2,8,3,4]
## 리스트 두개 합치기
mixlist.extend(mylist2)
print(mixlist)
