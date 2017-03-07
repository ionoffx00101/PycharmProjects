# 문자열을 반반으로 나눠주자
letters = "introducing python"

print(letters[:int(len(letters)/2)])
print(letters[int(len(letters)/2):])

# 문자열 길이를 반환하는 len
# 전체길이/2 하니까 9.0
# int가 아니라고 오류나서
# int()를 사용해서 변환해주었다.
