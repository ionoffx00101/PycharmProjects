# 040 문자열 분리
# 사용자로부터 '10:00:01'와 같은 형태로 시간을 입력 받은 후
# 해당 시간이 00:00:00 으로부터 몇 초가 지났는지를 출력하라.

# time = input()
time = "10:00:01"
times = time.split(':')
result = int(times[0])*3600+int(times[1])*60+int(times[2])
print(result)