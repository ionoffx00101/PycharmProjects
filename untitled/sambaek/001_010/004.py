# 두 개 수를 입력받으라는데 그걸 어떻게 해
# java는 Scanner 클래스 이용하면 되지만

# input,raw_input 이라는 게 있다
# input은 정수로 받는다
# raw_input은 문자열로 받는다
# > 내가 쓰는 파이썬3에서는 해당 함수가 사라진듯 그래서 input 쓰니까 문자열로 받아진거였어
# 이 문제에서는 두 수를 받으라고 했으니 둘 다 input을 쓰면 될거 같다.
first = input("입력 : ")
second = input("입력 : ")

result= first+second

print("first",first,"second",second,result)
# 그냥 더하니까 숫자가 문자열처럼 더해지지 계산이 안된다..

result= int(first)+int(second)
print("first",first,"second",second,result)
# int()를 써주었더니 정수형으로 변한 상태로 더하기가 된다
# int(), float(), str()...