def diag_sum(board, m, n):
    d1, d2 = {}, {}
    for i in range(m):
        for j in range(n):
            d1[i-j] = d1.get(i-j, 0) + board[i][j]
            d2[i+j] = d2.get(i+j, 0) + board[i][j]
    return d1, d2
    

def max_sum(board, m, n):
    d1, d2 = diag_sum(board, m, n)
    ans = -1
    temp = 0
    for i in range(m):
        for j in range(n):
            temp = d1[i-j]+d2[i+j]-board[i][j]
            ans = max(ans, temp)
    return ans
        
q = int(input())
while q:
    m, n = map(int,input().split())
    board = []
    for _ in range(m):
        board.append(list(map(int, input().split())))
    ans = max_sum(board, m, n)
    print(ans)
    q -= 1