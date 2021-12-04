#변수(variable)-----------------------
boyf = "남자친구"
name = "달님이"
age = 33
hobby = "쮸"
is_adult = age >40
print(age)
print(is_adult)
print("제 "+boyf+"는"+name+ "입니다.")
print(name+"는" + str(age)+"살 이구요 ,"+ hobby+"를 아주 좋아해요")
print(name+ "는 어른일까요?"+str(is_adult))

# str(33) #정수 33 을 문자형으로 바꿔주는 str
# 정수가, ++를 포함해 다른 문자들과 함께 프린트 문에서 쓰일때는 str로 감쌀것!!
# 불리언 대답이 나오는 것도 형변환 대상 !
####### can only concatenate str (not "int") to str ########
####### str에는 str만 연결시킬수있다.  ###########

print("제 나이는",age,"입니다.")

#더하기 대신 콤마로 연결시에는 str로 감싸지 않아도 오류가 나지 않아요
#대신 콤마는 한칸 띄워서 인식합니다.