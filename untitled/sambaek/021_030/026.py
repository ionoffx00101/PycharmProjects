lang = 'python'

print(lang.replace('p','P'))

# 실패 1
# lang.replace('p','P')
# print(lang)
# replace를 한번써놨다고 문자열이 변경된상태로 저장되는 건 아니였다
# print안에서 replace함수를 이용 문자열을 바꿔주고 출력하는 일회용 함수라고 봐야할 것 같다.

# 왜 자꾸 이런 오류가 뜨는 지 모르겠다. 컴파일에는 문제가 없다
# PEP 8: missing whitespace after ','

# 문제 026
# 파이썬 문자열은 변경할 수 없는 객체이다. replace 메서드를 사용하여 'python'을 'Python'으로 변경하라.
