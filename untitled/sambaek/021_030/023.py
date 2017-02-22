code = '         000660\n            '

print(code.strip())

# 문자열 잘라내기2
# 양쪽 끝의 공백 문자를 제거하는 경우 - str.strip:
# 모든 스페이스(' ')를 제거하는 경우 - str.replace():
# 모든 공백 문자를 제거하는 경우 - re모듈:
# 중복된 공백 문자를 제거하는 경우(예_ 스페이스바가 2개) - str.split()과 str.join():