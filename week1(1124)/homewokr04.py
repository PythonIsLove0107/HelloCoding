# 키보드로 입력한 점수(0 ~ 100)가 어느 학점에 해당하는지 구하는 프로그램
# 90 ~ A학점
# 80 ~ B학점
# 70 ~ C학점
# 60 ~ D학점
# 60점 미만 F학점

# score = int(input(이번학기 너의 수학 점수는?))
# if 89 < score <101:
#     print("A학점")
# elif 79 < score < 90
#     print("B학점")

'''
n = int(input('정수 n 를 입력하세요?'))
if n >= 90:
    print('A학점')
elif n >=80:
    print('B학점')
    
# 키보드로 입력한 점수(0 ~ 100)가 어느 학점에 해당하는지 구하는 프로그램
# 90 ~ A학점
# 80 ~ B학점
# 70 ~ C학점
# 60 ~ D학점
# 60점 미만 F학점

score = int(input(이번학기 너의 수학 점수는?))
if 89 < score <101:
    print("A학점")
elif 79 < score < 90
    print("B학점")
'''

n = int(input('정수 n 를 입력하세요?'))
if n >= 90:
    print('A학점')
elif n >=80:
    print('B학점')
elif n >=70:
    print('C학점')
elif n >=60:
    print('D학점')
else:
    print('F학점')
    
수업 마무리
중첩 if 문 for 문 다시 continue, break, pass
