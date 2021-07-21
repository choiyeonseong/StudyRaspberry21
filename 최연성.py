#  리스트 [1, 2, 3, ~ 100] 까지의 수 중에서 
# 3의 배수만 합한 합산 값과 
# 7의 배수의 합산값을 출력하는 파이썬 코드를 작성하세요. 
# 작성 후 '본인의이름.py'로 파일을 업로드 하세요.

three = 0
seven = 0
list=[]
for i in range(100):
    list.append(i)

for i in list:
    if(i%3==0):
        three+=i
    if(i%7==0):
        seven+=i

print('3의 배수의 합산: {0}, 7의 배수의 합산: {1}'.format(three, seven))