munja = input("입력 : ")
ban = int(input("숫자 입력 : "))
print('"',end='')
for a in range(ban):
    print(munja,end='')
    # print(munja) 했더니 줄바꿈되어서 표시된다
    # end='' 아까 배운걸 썼더니 줄바꿈 안 하고 표시된다.

print('"')