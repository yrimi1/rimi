# 슬라이싱-----------------------------
jumin = "890905-1234567"

print("성별 :" + jumin[7])  # 7번째 인덱스 값
print("연 :" + jumin[0:2])  # 0번째부터 2번째 "이전" 인덱스까지
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])

# print("생년월일 :"+jumin[0:6])
print("생년월일 :" + jumin[:6])  # 콜론으로 시작하면 처음부터~6직전까지
# print("뒤 7자리 :"+jumin[7:14])
print("뒤 7자리 :" + jumin[7:])  # 콜론으로 끝내면 7부터 ~ 끝까지

print("뒤 7자리(뒤에부터) :"+jumin[-7:]) #맨 뒤에서 7번째 부터 끝까지
