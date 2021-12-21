##집합(set)----------------------------
# 중복안됨. 순서없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set)  # 출력해도 3은하나..세트에는 중복이없으니까...
#
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])  # 이런식으로 세트를 정의 가능... 리스트만들어서 세트로 감싸기

# 교집합 (java.python 둘다가능)
print(java & python)
print(java.intersection(python))

#합집합 (java.python 둘중 하나 가능)
print(java | python)
print(java.union(python))

#차집합 (java 만 가능 , python불가)
print(java - python)
print(java.difference(python))

#python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java까먹음
java.remove("김태호")
print(java)
