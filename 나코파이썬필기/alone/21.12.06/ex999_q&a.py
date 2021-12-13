# Q. 당신은 cocoa서비스를 이용하는 택시 기사님 입니다.
# 50명의 승객과의 매칭기회가 있을 때, 총 탑승 승객수를 구하는 프로그램을 작성하시오

# 조건 1: 승객별 운행 소요시간은 5분~50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요시간 5분~15분 사이의 승객만 매칭해야합니다.

# 출력문 예제 
# [0] 1번째 손님 (소요시간 : 15분) 
# [ ] 2번째 손님 (소요시간 : 50분) 
# [0] 3번째 손님 (소요시간 : 5분) 
# ...
# 총 탑승 승객 : 2 분

from random import *

count = 0
maching = range(1, 51)  # 1에서 50까지의 리스트
runtime = int(random() * 49) + 1  # 1에서 50까지의 난수

for i in maching:
    runtime = int(random() * 49) + 1
    if 5 <= runtime <= 15:
        print("[o] {0}번째 손님 (소요시간: {1})".format(i, runtime))
        count +=1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1})".format(i, runtime))

print("총 탑승승객,{}명".format(count))
