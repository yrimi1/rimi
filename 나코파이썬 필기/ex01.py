# python = "dal rim love"
# # print(my_list.replace("rim","hrimi"))
# f = python.index("l")
# print(f)
# f2 = python.index("l",f+1)
# print(f2)

# bs = "tkfkdgksms ekfsladl djelrkTsl"
# ind = bs.index("e")
# print(ind)
# ind2 = bs.index("e",ind+1)
# print(ind2) 
#Q> 
s1 = "http://naver.com"
s2 = s1.replace("http://","")
s3 = s2.replace(".com","")

# s4 = s3[:3]
# s5 = len(s3)
# print(str(s4)+str(s5)+str(s3.count("e"))+"!")
print(str(s3[:3])+str(len(s3))+str(s3.count("e"))+"!")






### 나도코딩 3번 문제 사이트 별로 비밀번호 만들어주는 플그램 만들어용###
#예) http://naver.com 를 입력받으면...
#  http://제외
#  .com제외
#남은 글자 중 처음세자리 + 글자개수+ 글자 내 "e" 개수 + "!" 로 구성
# 생성된 비밀번호는 : van51!


# # s1 = "http://naver.com"
# s1 = input("주소를 입력해 주세요")
# s1 = "http://naver.com"
# s2 = s1.replace("http://","")
# s3 = s2.replace(".com","")
#
# # s4 = s3[:3]
# # s5 = len(s3)
# # print(str(s4)+str(s5)+str(s3.count("e"))+"!")
#
# print(str(s1)+" 사이트의 비밀번호는: "+str(s3[:3])+str(len(s3))+str(s3.count("e"))+"!"+"입니다.")



# s1 = "http://naver.com"
s1 = input("주소를 입력해 주세요")
s2 = s1.replace("http://","")
# s3 = s2.replace(s2[-4:],"")
s3 = s2.replace(s2[s2.index("."):],"")
# gofla8358@hanmail


# s2 = s1.replace("http://","")
# s3 = s2.replace(".com","")

# s4 = s3[:3]
# s5 = len(s3)
# print(str(s4)+str(s5)+str(s3.count("e"))+"!")

print(str(s1)+"의 비밀번호는: "+str(s3[:3])+str(len(s3))+str(s3.count("e"))+"!"+"입니다.")