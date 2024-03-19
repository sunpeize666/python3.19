'''
202195057 손패택
2024.03.19
'''
kor = input(" kor 점수 입력 : ")

eng = input(" eng 점수 입력 : ")

math = input(" math 점수 입력 :")

com = input(" com 점수 입력 : ")

sci = input(" sci 점수 입력 : ")

total = kor + eng + math + com + sci
avg = total / 5
porint ("총점 : ", (total))
porint ("평점 : ", (avg))
porint ("평점 : {:.2f}" .format(avg))
porint (f"평점 : ", forma(avg))





