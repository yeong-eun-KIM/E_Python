#ezen04-2
#파이썬 데이터 타입(자료형)
#리스트, 튜플

#리스트 자료형 (순서,중복,수정, 삭제 가능)

#선언
a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'powerful', 'health', 'feature']
e = [10,100, ['powerful', 'health', 'feature']]

#인덱싱
print()
print("d : ", type(d),d)
print("d : ", d[1])
print("d : ",d[0]+d[1]+d[1])
print("d : ",d[-1])
# health 출력
print("e : ",e[-1][-2])
# heal't'h 출력
print("e : ",e[-1][-2][-2])

#슬라이싱
print("d : ",d[0:1])
print("d : ",d[2:])

#연산
print()
print("c + d : ", c+d)
print("c : ", c *3)

#수정,삭제
print()
c[0] = 4
print("c : ", c)
c[1:2] = ['a','b','c']
print("c : ", c)
c[1] = ['a','b','c']
c[1:3] = []
print("c : ", c)
del c[3]
print("c : ", c)

#리스트 함수
a = [5,2,3,1,4]
print("a : ", a)

a.append(6)
print("a : ", a)

a.sort
print("a : ", a)

a.reverse
print("a : ", a)

print("a : ", a.index(5))

a.insert(2,7)
print("a : ", a)

a.remove(1)
print("a : ", a)

print("a : ", a.pop())
print("a : ", a.pop())

print("a : ", a)


print("a : ", a.count(4))

ex = [8,9]
a.extend(ex)
print("a : ",a)

'''while a :
    1 = a.pop()
    print(2 is 1)'''

#===================================================#

#튜플 (순서, 중복 가능 / 수정, 삭제 불가)
'''
    튜플(tuple) 자료형은 리스트와 유사
    리스트는 대괄호[]를 이용하지만, 튜플은 소괄호() 또는 괄호 생략
    값이 변경되면 안되는 경우, 튜플을 사용하면 효과적임
'''

#선언
a = ()
b = (1,)
c = (1,2,3,4,)
d = (10, 100, 'powerful', 'health', 'feature')
e = (10,100, (10, 100, 'powerful', 'health', 'feature'))

#인덱싱
print()
print("d : ", type(d),d)
print("d : ", d[1])
print("d : ",d[0]+d[1]+d[1])
print("d : ",d[-1])

arr= [5]*8
print(arr)

arr = [[0] * 5 for _ in range(4)]
print(arr)

arr = [[i] * 5 for i in range(4)]
print(arr)

arr = [[i*5] + j for j in range(5) for i in range(4)]








