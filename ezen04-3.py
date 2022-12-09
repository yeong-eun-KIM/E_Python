#ezen04-3
#파이썬 데이터 타입(자료형)
#딕셔너리, 집합 자료형

#딕셔너리
a = {'name':'ezen',"phone":"01012345678","birth": "901224"}
b = {0:"hello ezen"}
c = {"arr" : [1,2,3,4]}

#출력
print("a : ", a['name'])


a['address'] = "seoul"
print("a : ",a)

# rank [1,2,3]

a['rank'] = [1,2,3]
print("a : ",a)

arr1 = ['컴퓨터','키보드','모니터']
arr2 = ['computer','keyboard','monitor']

data = {}

for i in range(3) :
    data[arr1[i]] = arr2[i]

print(data)

print(data.keys)

data = {}
data['apple'] = '사과'
data['banana'] = '바나나'
data['carrot'] = '캐럿'

for key in data.keys() :
    print(key,data[key])

print(data.items())

#특정한 데이터의 등장 횟수

data = [1,3,3,5,4,4,1,4]
