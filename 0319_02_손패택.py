'''
202195057손패택
2024.03.19
输入上边下边高度
写一个求梯形宽度的程序

梯形宽度=（上边+下边）*高/2
各边的长度以整数形式接受并储存在变量中。
变量名：上边=>top
下边=>bottom
高度=>height
宽度=>area

1.计算梯形的上边，下边，高度。
2.计算提醒的面积
3.梯形输出
'''
top=int(input("웟변을 입력하시오 : "))
bottom = int(input("아랫변을 입력하시오 : "))
height = int(input("높이를 입력하시오 : "))

area = ((top + bottom) * height) / 2
print(area)

print(f"윗변 {top}, 아랫변 {bottom}, 높이 {height}인")
print(f"윗변 {top}, 아랫변 {bottom}, 높이 {height}인")
