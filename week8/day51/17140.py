import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(3)]

time = 0
def KK() :
    if r-1 < len(data) and c-1 < len(data[0]) :
        if data[r-1][c-1] == k :
            return True
    return False

def UPDATE() :
    # 개수 세기
    temp_matrix = []
    max_value = 0
    for i in range(len(data)) :
        nums = set(data[i])
        temp = []
        for num in nums :
            if num == 0 : # 값이 0일 경우 무시
                continue
            temp.append((num, data[i].count(num))) # (수, 등장 횟수) 형태로 추가
        max_value = max(max_value, len(temp) * 2)
        temp_matrix.append(temp)

    # 정렬 작업 수행
    for i in range(len(temp_matrix)) :
        temp_matrix[i].sort(key=lambda x: (x[1], x[0])) # 등장횟수 커지는 순 -> 수가 커지는 순

    # 길이 맞추고 배열에 삽입
    for i in range(len(temp_matrix)) :
        value = []
        for j in range(len(temp_matrix[i])) :
            value.append(temp_matrix[i][j][0])
            value.append(temp_matrix[i][j][1])
        # 0으로 채운다
        value.extend([0] * (max_value - len(value)))
        data[i] = value

while time < 101 :
    # k 값이 일치한지 확인
    if KK() :
        print(time)
        break

    time += 1 # 시간 증가
    if len(data) >= len(data[0]) : # R 연산
        UPDATE()
    else : # C 연산
        data = list(map(list, zip(*data))) # 행과 열 바꾸기
        UPDATE()
        data = list(map(list, zip(*data))) # 다시 행과 열 바꾸기
else :
    print(-1)