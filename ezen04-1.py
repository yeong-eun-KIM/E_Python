#ezen04-1
#파이썬 데이터 타입(자료형)
#리스트, 튜플
#리스트 - 가변, 문자열 - 불변

odds = [1,3,5,7,9]
print(odds)

#일반적으로 리스트와 각 원소는 같은 자료형이 되도록 쓰이지만 서로 다른 자료형의 데이터가 들어갈 수 있음
data = ["hello", 7, 8.5]
print(data)

#리스트에 대하여 인덱싱과 슬라이싱을 사용가능
evens = [2,4,6,8,10,12,14,16]
print(evens)
print(evens[0:5])

#리스트 연결 : 리스트끼리 더할 수 있으나, 단순히 이어붙인 결과임
a = [1,2,3,4,5]
b = [6,7,8,9,10]

print(a+b)

#리스트 중첩
arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(arr)
print(arr[0][1]) # 2 출력
print(arr[2][2]) # 13 출력

#리스트 주요 메서드
'''
    insert(삽입할 인덱스, 삽입할 원소)
    append(삽입할 원소)
    remove(삭제할 원소)
    sort()
'''

arr = [1,3,4]
print(arr)

arr.insert(1,2)
print(arr)

arr.append(5)
print(arr)

arr.remove(3)
print(arr)

arr.sort(reverse=True)
print(arr)

arr = []

for x in range(10) :
    arr.append(x)

print(arr)

arr = []
row1 = [1,2,3,4,5]
arr.append(row1)
print(arr)

row2=[6,7,8,9,10]
arr.append(row2)
print(arr)

#리스트 컴프리핸션 (2차원 이상의 리스트 초기화 시 사용)
#원소를 8개 포함하는 1차원 리스트 초기화
arr = [5] * 8
print(arr)

# 4 x 5 크기를 갖는 2차원 리스트 초기화
arr = [[0] * 5 for _ in range(4)]
print(arr)