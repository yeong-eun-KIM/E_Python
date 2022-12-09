#ezen03-2
#파이썬 데이터 타입(자료형)
#문자열, 문자열 연산, 인덱싱, 슬라이싱

#문자열
str1 = "Happy New Year"
str2 = 'newYear'
str3 = """what is the name of the car?"""
str4 = '''three and single'''

#문자열 타입 출력
print(str1)
print(str2)
print(str3)
print(str4)

#문자열 길이 출력
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

#빈 문자열
str_t1 = ''
str_t2 = str()

#빈문자열 타입 출력
print(type(str_t1),len(str_t1))
print(type(str_t2),len(str_t2))

#문자열 인덱싱(indexing) : 문자열에 포함된 특정한 하나의 문자를 얻을 수 있음. 첫번째 문자는 인덱스에 해당
a = "hello"
print(a[0])
print(a[-1])

#문자열 슬라이싱(slicing) : 부분 문자열(substring)을 얻기 위해 사용
#슬라이싱은 두개의 인덱스로 구성, 변수명[시작 인덱스:끝인덱스]

a = "hello world"
#인덱스 3까지의 접두사를 가져오시오
print(a[0:4])

#인덱스 2부터의 접미사를 가져오시오.
print(a[2:])

#중간에 있는 부분문자열을 출력
print(a[-4:-1])

#문자열 인덱싱을 할 때는 범위를 벗어난 경우 오류 발생
#슬라이싱은 범위가 벗어나도 알맞게 처리

#파이썬에서 문자열은 값을 변경할수 없기 때문에, 불변(immutable)이라고도 함
# a[3] ='b' 오류 발생
