'''
구구단 출력 프로그램을 만들어 보시오
사용자로부터 출력할 단을 입력 받고, 해당 구구단을 출력하는 프로그램입니다
'''

x = int(input("몇 단을 출력할까요?>>>"))
i = 1
while i <10:
    print(x,'*',i,'=',x*i)
    i += 1

print()

y = int(input("몇 단을 출력할까요?>>>"))
for i in range(1,10) :
    print(y,'*',i,'=',y*i)