## 반복문에서 쓰이는 continue와 break... 흐름을 여러번 읽어보기
absent = [2,5] #결석
no_book = [7]
for student in range (1,11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘수업 여기까지. {}는 교무실로 따라와".format(no_book))
        break
    print("{0},책을 읽어봐".format(student))