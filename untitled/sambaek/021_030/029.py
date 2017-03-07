# 문제 029
# 사용자로부터 웹페이지 주소를 입력받고 도메인을 출력하라
# 도메인은 .com, .net, .org만 지원 한다 www는 반드시 입력

# 사용자한테 주소 입력받기
address = input()

print('domain : '+address[address.rindex('.'):address.rindex('.')+4])


#####################################################################################
# 실패한 영역
# 사용자한테 주소 입력받기
# address = input()
# address = 'http://www.wikidocs.net/edit/page/7022'
# 도메인이 들어있는 배열 만들어 두기
# domain = ['.com','.net','org']
# 멤버십 테스트(Membership Test) : in
# address.find(domain)
# i = address.index('.')

# print('domain : '+address[address.index('.'):address.index('.')+4])
# print('domain : '+address[address.index(domain):address.index('.')+4])
# if address in domain:
#     print('domain : '+address[address.rindex('.'):address.rindex('.')+4])
# else:
#     print('그런 주소는 지원하지 않습니다.')
