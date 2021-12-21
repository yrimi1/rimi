############ while 문 2###########
# 손님 확인후 커피주기 원하는 손님아니면 다시반복

customer = "림이"
person = "Unknown"

while person != customer: # 손님이 림이가 아닌동안에 반복문을 돌다가
                          # 원하는손님이 오면 반복문을 탈출한다.
    print("{},커피가 준비되었습니다.".format(customer))
    person = input("이름이 뭐예요?")
