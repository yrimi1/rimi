## 분기 이런상황에서는 이코드 저런상황에서는 저코드

w = input("날씨입력")  ## input은 항상 문자로 입력받음
if w == "비":
    print("우산을 챙기세요 ")
elif w == "미세먼지":
    print("마스크")
else:
    print("필요없음")

t = input("기온입력")
if t == 1:
    print("1도")
elif t == 2:
    print("2도")
else :
    print("ㄴㄴ")
