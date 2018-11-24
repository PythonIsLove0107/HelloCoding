# if 사용
# 정수를 입력하세요?? 입력받은 후 양수일경우 양수로, 음수일 경우 음수로
'''
no_1 = int(input("정수를 입력하세요"))
if no_1 > 0:
    print(no_1, "은/는 양수입니다.")
elif no_1 == 0:
    print(no_1, "은 0입니다.")
else :
    print(no_1, "은/는 음수입니다.")
'''

#### 위는 내가 짠 코드

n = int(input('정수를 입력하세요?'))
if n > 0:
    print(n, '는 양수입니다.')
else:
    print(n, '는 음수입니다.')