# Q. 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# http://부분은 제외 => naver.com
# 처음 만나는 점 이후 부분은 제외 => naver
# 남은 글자 중 처음 세자리 + 글자갯수 + 글자내 'e'개수 + !로 구성
# 생성된 비밀번호 : nav51!

## 1번 방법---------------------------------------------------
# s1 = "http://naver.com"
# s2 = s1.replace("http://","")
# s3 = s2.replace(".com","")
# s4 = s3[:3]
# s5 = len(s3)
# print(str(s4)+str(s5)+str(s3.count("e"))+"!")
##------------------------------------------------------------


## 2번 방법-----------------------------------------------------------------------
# s1 = input("주소를 입력해 주세요")
# s1 = "http://naver.com"
# s2 = s1.replace("http://","")
# s3 = s2.replace(".com","")
# print(str(s1)+" 사이트의 비밀번호는: "+str(s3[:3])+str(len(s3))+str(s3.count("e"))+"!"+"입니다.")
## -------------------------------------------------------------------------------

## 3번 방법----------------------------------------------------------
s1 = input("주소를 입력해 주세요")
s2 = s1.replace("http://","")
# s3 = s2.replace(s2[-4:],"")
s3 = s2.replace(s2[s2.index("."):],"")
print(str(s1)+"의 비밀번호는: "+str(s3[:3])+str(len(s3))+str(s3.count("e"))+"!"+"입니다.")
##-------------------------------------------------------------------------