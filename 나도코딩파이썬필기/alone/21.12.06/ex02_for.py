##-----------반복문 (for)------------------
# print("대기번호 : 1 ")
# print("대기번호 : 2 ")
# print("대기번호 : 3 ")
# print("대기번호 : 4 ")

for waiting_1 in [0,1,2,3,4]: #배열의 안 요소들이 처음부터 끝까지 차례대로 웨이팅변수에 들어가서 for 문을 돈다.
    print("대 기 번 호:{}".format(waiting_1))

for waiting_2 in range(5): #0~4 까지 들어가는...
    print("대기 번호:{}".format(waiting_2))

for waiting_3 in range(1,101):
    print("대기번호:{}".format(waiting_3))

starbucks = ['정달님','유내림','이동준','박명회']
for customer in starbucks:
    print("{}님..,커피가 준비되었습니다.".format(customer))