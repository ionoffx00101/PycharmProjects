for (a) in [2,3,4,5,6,7,8,9]:

    for (b) in [1,2,3,4,5,6,7,8,9]:
        print(a, " * ", b, " = ", a * b)


# 결과는 잘 나왔다
# 리스트를 저렇게 꼭 만들어줘야하나.

# range(시작,끝,증가값)
# 그리고 for문 변수에 괄호 안쳐도 된다..
# for 변수 in list ㅇㅇ

for i in range(2,10):
    for j in range(1,10):
        print(i, " * ", j, " = ", i * j)
