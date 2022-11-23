'''
로또 예상번호 추출 프로그램을 구현하려고 합니다.
다음 조건에 따라 프로그램을 완성해 보시오
    1) 로또 번호를 6개를 생성한다
    2) 로또 번호는 1~45까지의 랜덤한 번호다
    3) 6개 숫자 모두 달라야 한다
    4) get_random_number() 함수를 사용해서 구현
    출력 예) 1 8
'''
import random

def get_random_number():
    number = random.randint(1,45)
    return number

list = []
while len(list) < 6 :
        num = random.randint(1,45)
        if num not in list:
            list.append(num)
            continue
print(list)

lotto_num = []
count = 0
while True:
    if count > 5:
        break
    randon_num = random.randint(1,45)
    if randon_num not in lotto_num:
        lotto_num.append(randon_num)
        count += 1

print(sorted(lotto_num))
