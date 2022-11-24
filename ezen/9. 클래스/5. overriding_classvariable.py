'''
상속의 업그레이드
    - 클래스 변수 (인스턴스들이 모두 공유하는 변수)
    예
    드래곤 클래스에 인스턴스 속성을 추가하기
    부모 클래스에 클래스 변수 추가하기
    
'''
# 부모클래스
class Monster:
    max_num = 1000 #클래스변수
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1 #인스턴스 생성할때마다 1씩 감소

    def move(self):
        print(f"[{self.name}]움직이기")
        
