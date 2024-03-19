'''
2024.03.19
202195057 손패택
'''
name = input("이름을 입력하시오 : ")

print(name, "남 황영합니다.")
print("{}님 황영합니다." .format(name))
print(f"{name}님 황영합니다.")

kor = input("국어 점수 입력 : ")

math = input("수학 점수 입력 : ")

total = kor + math

print(f"두 과묵의 점수는 {total}점입니다.")
eng = int(input("영어 점수 입력 : "))
com = int(input("컴퓨터 점수 입력 : "))

total = eng + com
print(f"두 과묵의 점수는 {total}점입니다.")

print("kor 번수에 저장된 자료형 ", type(kor))
print("kor 번수에 저장된 자료형 ", type(math))
print("kor 번수에 저장된 자료형 ", type(eng))
print("kor 번수에 저장된 자료형 ", type(com))