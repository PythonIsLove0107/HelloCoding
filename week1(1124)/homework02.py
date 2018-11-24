# # for 와 range를 사용하여 원하는 단을 입력하세요? 입력 받은 후 구구단을 출력하라

# fir = input("원하는 단을 입력하세요!")
# for i in range(1, 10):
#     print(str(fir) * str(i)) = int(fir)*i



#키보드로 1개의 구구단 1개의 단을 입력받아서 출력하는 프로그램 작성
dan = int(input('원하는 단을 입력하세요?'))
for i in range(1, 10):          # 1 ~ 9
    # print(dan, '*', i, '=', dan * i)
    print('{} * {} = {}'.format(dan, i, dan*i))