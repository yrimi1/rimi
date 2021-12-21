## if문..분기!!!..... 이런상황에서는 이코드 저런상황에서는 저코드

weather = input("날씨 입력해 주세요")  ## input은 항상 문자열 형태로 입력받음
if weather == "비" or weather == "눈":
    print("우산을 챙기세요 ")
elif weather == "미세먼지":
    print("마스크 쓰세오")
else:
    print("걍 가라")

temp = int(input("기온입력해주세요"))  ## 문자열로 입력받은 값을 정수형을 바꿔서 저장
                                    ## 만약 int로 감싸주지 않는다면 숫자1을 입력해도
                                    ##정수로 받아들이지 못해서 else구문을 토할것..
if 30 <= temp:
    print("겁나..더움...")
elif 10 <= temp and temp < 30:
    print("적정온도")
elif 0 > temp:
    print("추브요")
