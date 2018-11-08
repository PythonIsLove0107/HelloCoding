#참고_4장 1번 연습문제

list_a = [1, 2, 3, 4, 5]
min_value = list_a[0]
for element in list_a:
    if element < min_value:
        min_value = element
print("최소값:", min_value) 


list_b = [1, 2, 3, 4, 5]
max_value = list_a[0]
for element_1 in list_b:
    if element_1 > max_value:
        max_value = element_1
print("최대값:", max_value) 


#참고_3장 3번 연습문제

str_input = input("태어난 해를 입력해주세요> ")
birth_year = int(str_input) % 12
tti = ["원숭이", "닭", "개", "돼지", "쥐", "소", "범", "토끼", "용", "뱀", "말", "양"]
print(tti[birth_year], "띠입니다.")