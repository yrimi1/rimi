# 한줄 삭제 ctrl +x
# 키위치 노상관 아랫줄 Shift + Enter

#1명 치킨 ,3명 커피
#댓글은 20명작성 아이디는 1~20
#중복불가
#random 모듈의 shuffle와 sample 활용
from random import *

mylist = range(1,21)

mylist = list(mylist)
print(mylist)

shuffle(mylist)
print(mylist)

dagnchem = sample(mylist,4)
print(dagnchem)
#
# print("-----당첨자 발표-----")
# print("치킨 당첨자는:"+str(dagnchem[:1]))
# print("커피 당첨자는:"+str(dagnchem[1:]))
# print("축하 합니다.")

print("치킨{}번 입니다.".format(dagnchem[:1]))
print("코피{}번 입니다.".format(dagnchem[1:]))








# 답
# from random import *
# a = range(1,21)
# print(type(a)) #class range
# a = list(a) ## class list
# shuffle(a) ## 섞기
# b = sample(a,4)
# 
# print("----당첨자 발표----")
# print("치킨 당첨자 :"+str(b[:1]))
# # print("커피 당첨자 :"+str(a[1])+"번"+str(a[2])+"번"+str(a[3])+"번")
# print("커피 당첨자 :"+str(b[1:]))
# print("축하합니다.")

