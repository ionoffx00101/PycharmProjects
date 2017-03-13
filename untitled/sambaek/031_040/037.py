# 037 경로 분리
# 사용자로부터 윈도우 디렉터리 경로를 입력 받은 후 가장 최종 디렉터리를 출력하라.

# path = input();
path = "c:\\program files\\python"

# 뒤에서부터 \을 검색해서 끝에서부터 그 \까지를 출력하면 되려나
# index로 해당 위치 찾고 슬라이싱이나 substring으로 해당 부분만 출력하면 될거 같은데
# path[\찾은 부분 : 끝]
print(path[path.rindex("\\"):])

# 결과
# \python
# \ 한개 더 없애는 방법은 없는 걸까