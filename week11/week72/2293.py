import sys
input = sys.stdin.readline

def Solve():
    global n, k
    coins = [int(input()) for _ in range(n)]
    knapsack = [1] + [0]*k
    for coin in coins:
        for col in range(coin, k+1):
            knapsack[col] += knapsack[col - coin]
    return knapsack[k]

n, k = [*map(int, input().split())]
print(Solve())