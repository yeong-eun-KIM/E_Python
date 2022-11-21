# 제어문 - 조건문, 반복문
# ex) 기존 비밀번호 = "0111"
#     입력한 비밀번호 = "0111"
#     만약 비밀번호를 정확히 입력했으면 => 로그인 성공!
#                   입력안했으면 => 아무것도 입력하지 않았습니다.
#                   일치하지 않으면 => 로그인 실패!


origin_pass = "0111"
input_pass = input("비밀 번호를 입력하세요>>")
if origin_pass == input_pass :
    print("로그인 성공!")
elif input_pass == '' :
    print("아무것도 입력하지 않았습니다.")
else :
    print("로그인 실패!")


