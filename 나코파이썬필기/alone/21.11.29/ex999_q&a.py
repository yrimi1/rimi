# 한줄 삭제 ctrl +x
# 키위치 노상관 아랫줄 Shift + Enter


#1명 치킨 ,3명 커피
#댓글은 20명작성 아이디는1~20
#중복불가
#random 모듈의 shuffle와 sample 활용

#예)-----------------------
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,3))
#---------------------------

# from random import *
# users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #list
# users = range(1,21)
# print(users)
# users = list(users)
# # shuffle(users) #섞음
# print(users)
# b = sample(users,1)
# print(b)
# print("치킨 당첨자는"+str(b)+"번 입니다.")
# print("커피 당첨은"+str(sample(users,1))+"번"+str(sample(users,1))+"번"+str(sample(users,1))+"번 입니다.")
#


# 한줄 삭제 ctrl +x
# 키위치 노상관 아랫줄 Shift + Enter


from random import *
a = range(1,21)
print(type(a)) #class range
a = list(a) ## class list
shuffle(a) ## 섞기
b = sample(a,4)

print("----당첨자 발표----")
print("치킨 당첨자 :"+str(b[:1]))
# print("커피 당첨자 :"+str(a[1])+"번"+str(a[2])+"번"+str(a[3])+"번")
print("커피 당첨자 :"+str(b[1:]))
print("축하합니다.")
