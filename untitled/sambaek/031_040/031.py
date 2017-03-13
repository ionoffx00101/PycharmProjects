# 031 문자열 자르기
# 사용자로부터 파일명을 입력 받은 후 확장자만 출력하는 프로그램을 작성하라.

filename = input()
# filename = 'report.docx'

# print(filename.split('.'))
print(filename.split('.')[1])