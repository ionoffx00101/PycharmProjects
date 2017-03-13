# 039 문자열 개수 확인
# 'Python python pYthon java Java'에서 대소문자를 구분하지 않고 사용된 python 문자열의 개수를 출력하라.

# 생각 1
# 대소문자 상관 없이 단어 개수 검색해주는 메소드가 있을 것같다

# 생각 2
# 전체 문자열을 대문자 또는 소문자로 변환 시킨 후 검색한다
# s.upper or s.lower()

# 생각 2
s = 'Python python pYthon java Java'
print(s.lower().count('python'))