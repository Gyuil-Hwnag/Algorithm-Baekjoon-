from collections import deque

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def rotate(x, d, k):
    dq = deque()
    dq.extend(graph[x])
    if d == 0:
        dq.rotate(k)
    else:
        dq.rotate(-k)
    graph[x] = list(dq)


def change_avg():
    avg_count = 0
    all_sum = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                avg_count += 1
                all_sum += graph[i][j]
    if avg_count == 0:
        return False
    avg = all_sum / avg_count
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if graph[i][j] > avg:
                    graph[i][j] -= 1
                elif graph[i][j] < avg:
                    graph[i][j] += 1
    return True

def solve(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    value = graph[x][y]
    graph[x][y] = 0
    count = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > ny or ny >= m:
                if y == 0:
                    ny = m-1
                elif y == m-1:
                    ny = 0
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] == value:
                        count += 1
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        dq.append((nx, ny))
    if count == 0:
        graph[x][y] = value
    return count


for _ in range(t):
    x, d, k = map(int, input().split())
    check_sum = 0
    for i in range(n):
        check_sum += sum(graph[i])
        if (i+1) % x == 0:
            rotate(i, d, k)
    if check_sum == 0:
        break
    else:
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and graph[i][j] != 0:
                    cnt += solve(i, j)
        if cnt == 0:
            change_avg()

res = 0
for i in range(n):
    res += sum(graph[i])

print(res)