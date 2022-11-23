'''
순신은 lily라는 이름의 교환학생과 친해지게 되었습니다
영어를 잘하지 못한 순신은 lily에게 한국어를 가르쳐 주기 위해
한국어 연습 프로그램을 만들게 되었습니다
- 연습할 한국어가 담긴 리스트를 만든다
- 리스트에서 순서대로 단어를 가져와 화면에 출력한다
- 프로그램 사용자는 단어를 그대로 입력하고
- 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료
'''

# 전체 문제 개수 : 4개
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개
# len(word_list)
list = ['사랑해', '귀엽다', '고마워', '행복해']
total = len(list)
non_correct = 0
print("Let's Learning Korean")
for i in list :
    print(i)
    typing = input(">>>")
    if i != typing :
        non_correct += 1
print("전체 문제 개수 : ", total)
print("맞힌 문제 개수 : ", total-non_correct)
print("틀린 문제 개수 : ", non_correct)

