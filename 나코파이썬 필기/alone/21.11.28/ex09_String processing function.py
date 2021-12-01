# # 문자열 처리 함수--------------------------------
python = "Python is Amazing"

print(python.lower()) #모두 소문자 만들기
print(python.upper()) #모두 대문자 만들기
print(python[0].isupper())  # 파이썬이라는 문자열의 0번째인덱스값이 대문자냐? True
print(len(python))  # 파이썬이라는 문자열의 길이 반환
print(python.replace("Python", "java"))  #파이썬이라는 문자열에서 python을 찾아서 java로 바꾸어라



index = python.index("n")  #파이썬이라는 문자열에서 'n'은 몇번째 인덱스에있나요? index와 find는 같은기능한다..
print(index)
index = python.index("n",index+1) #index+1 부분이 시작부분... 6번쨰 인덱스 부터 n을 찾아줘요
print(index)
print(python.find("n"))   #파이썬이라는 문자열에서 'n'은 몇번째 인덱스에있나요? index와 find는 같은기능한다.. 단...


#### 파인드와 인덱스의 차이 ####
#문자열 내에 없는것 검색시....
print(python.find("java")) #파이썬이라는 문자열에서 자바를 찾아라....단,원하는 값이 없을떄는 -1반환 한다.
# print(python.index("java")) # 파이썬이라는 문자열에서 자바의 인덱스 값을 찾아라....단, 없을떄는 오류를 내고 프로그램 종료됨 (하이출력안됨.)
print("Hi") # 파인드와 인덱스의 차이


print(python.count("n")) #파이썬에서 n이 몇번 나오는가?


