import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 연결된 구역을 하나의 선거구로 만들기
# (현재 위치 x, 현재 위치, x 최소 값, y 최소 값, x 최대 값, y 최대 값, 몇번째 선거구인지)
def DFS(cx, cy, min_r, min_c, max_r, max_c, num):
    people[num] += city[cx][cy]  # 현재 위치 인구 수를 저장
    visited[cx][cy] = True  # 현재 위치를 방문 처리

    for d in range(4):
        nx = cx + dx[d]  # 다음 위치 x
        ny = cy + dy[d]  # 다음 위치 y

	# x, y 각각 최소, 최대 값 사이에 존재하면서 
        if min_r <= nx < max_r and min_c <= ny < max_c:
            if not visited[nx][ny]:  # 아직 방문하지 않은 위치인 경우 dfs 반복
                DFS(nx, ny, min_r, min_c, max_r, max_c, num)


n = int(input())
city = [[0 for _ in range(n + 1)]]  # 주어지는 구역 정보 저장 (0행 0열 0값 추가)
for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp.insert(0, 0)
    city.append(tmp)

res = 40000

# 전체 구역을 차례대로 기준점으로 선정
for x in range(1, n):
    for y in range(1, n):
    	# 각 기준점 안에서 경계선 길이 구하기
        for d1 in range(1, y):
            for d2 in range(1, n - y + 1):
            	# 선택한 기준점과 경계선의 길이가 주어진 범위 조건에 해당하는 경우
                if x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    people = [0] * 5  # 각 선거구의 인구 수를 저장할 배열
                    visited = [[False] * (n + 1) for _ in range(n + 1)]  # 각 구역을 방문했는지 확인할 배열

		    # 경계선 찾아서 방문처리 후 5번 선거구 인원수 추가
                    for i in range(d1 + 1):
                        if not visited[x + i][y - i]:
                            visited[x + i][y - i] = True
                            people[4] += city[x + i][y - i]

                    for i in range(d2 + 1):
                        if not visited[x + i][y + i]:
                            visited[x + i][y + i] = True
                            people[4] += city[x + i][y + i]

                    for i in range(d2 + 1):
                        if not visited[x + d1 + i][y - d1 + i]:
                            visited[x + d1 + i][y - d1 + i] = True
                            people[4] += city[x + d1 + i][y - d1 + i]

                    for i in range(d1 + 1):
                        if not visited[x + d2 + i][y + d2 - i]:
                            visited[x + d2 + i][y + d2 - i] = True
                            people[4] += city[x + d2 + i][y + d2 - i]

		    # 각 구역을 연결하여 선거구를 확인하고 인원수 확인 
                    DFS(1, 1, 1, 1, x + d1, y + 1, 0)
                    DFS(1, n, 1, y + 1, x + d2 + 1, n + 1, 1)
                    DFS(n, 1, x + d1, 1, n + 1, y - d1 + d2, 2)
                    DFS(n, n, x + d2, y - d1 + d2, n + 1, n + 1, 3)

		    # 5번 선거구 안쪽 인구 수 파악하기
                    for i in range(n + 1):
                        for j in range(n + 1):
                            if not visited[i][j]:
                                people[4] += city[i][j]

		    # 최소 인구 차 저장하기
                    res = min(res, max(people) - min(people))

print(res)