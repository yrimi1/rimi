cabinet = {"A-74":"정달님", "A-100":"유내림"} #이렇게 스트링형 키 선언도 가능하다.
print(cabinet["A-74"])
print(cabinet.get("A-100"))


#새손님 
cabinet["A-74"] = "달님ver.4"
cabinet["C-20"] = '조세호'
print(cabinet)


# 간 손님
del cabinet["C-20"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#Value들만 출력
print(cabinet.values())

#key ,value 쌍으로 출력 (item)
print(cabinet.items())


#캐비넷 비우기(clear)
cabinet.clear()
print(cabinet)