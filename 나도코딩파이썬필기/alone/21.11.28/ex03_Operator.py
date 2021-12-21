# 연산자(Operator)----------------------------
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)

print(2 * 3)
print(2 ** 3)  ### 2를 3번 거듭제곱하겠습니다. 2,4,8

print(5 % 3)  ### 나머지
print(5 / 3)  # 단순 나누기
print(5 // 3)  ### 나눠서 몫만 출력

print(10 > 3)  # True
print(4 >= 7)  # False
print(10 < 3)  # False
print(5 <= 5)  # Trur

print(3 == 3)  # True  같다는 == 두개쓸것.
print(4 == 3)  # Flase
print(3 + 4 == 7) #True


print(1 != 3)  ## != 같지않다
print(not (1 != 3))

print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # 둘다 만족시 트루

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # 둘중 하나 만족시 트루

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False
