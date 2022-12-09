# ezen02-2
# 파이선 기초 코딩
'''
python m venv 가상환경이름
    Script\activate.bat 가상환경 진입
    script\deactivate.bat 가상환경 해제

    pip install simplejson
    show
    uninstall
    list

    command : code
'''

import sys

# Python 3.x 입력 인코딩
print(sys.stdin.encoding)

# Python 3.x 출력 인코딩
print(sys.stdout.encoding)

myName = "Ezen"

#조건문
if myName == "Ezen":
    print("일치")

이름="이젠"
print(이름)

def 인사():
    print("아듀 2022년,해피뉴이어")

인사()

#클래스
class Cookie:
    pass

#객체 생성
cookie = Cookie()

#객체 정보 출력
print(id(cookie))

# 외부 설치 패키지 테스트
import simplejson as json
test_dict = {'1' : 95, '4' : 77, '3' : 65, '5' : 100, '2' : 88} #map 방식

print(json.dumps(test_dict,sort_keys=True, indent=4 * ''))
