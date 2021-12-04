# 문자열 포멧(String format)--------------------------
# 방법 1
print("나는 %d살 입니다." % 20)  # %d 정수 업력
print("나는 %s을 좋아해요" % "파이썬")  # %s 문자열 입력
print("Apple 은 %c로 시직해요" % "A")  # %c 문자 입력
# 구분없이 %s 로만 쓰면 프리패스!!
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨강"))

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")