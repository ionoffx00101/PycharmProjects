def sume(a,b):
    return a+b

x = 8
y = 9
z = sume(x,y)
print(z)

def me():
    print('dit is mijn python')

me()

def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
print(result) #두개의 값이 따로 옴 .여기서는 (7,12)

sum,mul=sum_and_mul(3,4) #이렇게 하면 두개의 값을 따로 넣어줄수있음

print(sum)
print(mul)