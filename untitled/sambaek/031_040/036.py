# 036 인덱싱 에러
# 다음 코드의 결과를 예상해보고 에러가 발생한 이유를 설명하라.

t = 'python'
t[100]

# Traceback (most recent call last):
#   File "<pyshell#339>", line 1, in <module>
#     t[100]
# IndexError: string index out of range

# //

# 예상
# 배열 크기 관련 오류가 뜰 것같다

# 이유
# t 변수 안에 들은 것보다
# 내가 호출한 것이 크다
# 내가 호출한 것은 존재하지 않는 것이다.
