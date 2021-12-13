############## 함수 (function)################
# 함수는... 어떤 역할을 하는 박스
def open_account():
    print("해로운 계좌를 개설하였습니다.")


# print(open_account()) (..X..)
# open_account()

def deposit(balance, momey):
    print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance + momey))
    return balance + momey


def withdraw(balance, momey):
    if balance >= momey:
        print("출금이 완료되었습니다.잔액은 {}원 입니다.".format(balance - momey))
        return balance - momey
    else :
        print("잔액이 부족합니다.잔액은 {}원 입니다.".format(balance))

def withdrow_night(balance,money):
    commission = 100 #수수료 100원
    return commission, balance - money - commission


balance = 0  #잔액
balance = deposit(balance, 1000)
balance = withdraw(balance,2000)
balance = withdraw(balance,500)
commission,balance = withdraw(balance,500)
print("수수료는 {0}원 입니다. 잔액은 {1}원 입니다.".format(commission,balance))