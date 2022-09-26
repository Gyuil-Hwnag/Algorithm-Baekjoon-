import sys
input = sys.stdin.readline

def MERGE_SORT(A, p, r):
    if(p < r and cnt <= K):
        q = (p + r) // 2
        MERGE_SORT(A, p , q)
        MERGE_SORT(A, q + 1, r)
        MERGE(A, p, q, r)
        
def MERGE(A, p, q, r):
    global cnt, res
    i, j = p, q + 1
    tmp = []
    
    while i <= q and j <= r:
        if(A[i] <= A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
        
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i, t = p, 0
    
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == K:
            res = A[i]
            break
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
res = -1

MERGE_SORT(A, 0, N - 1)
print(res)