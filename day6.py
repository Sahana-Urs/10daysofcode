def next_moves(a,b,i,j,n):
    M = ((a+i,b+j),(a+i,b-j),(a-i,b+j),(a-i,b-j),
         (a+j,b+i),(a+j,b-i),(a-j,b+i),(a-j,b-i))
    return {(a,b) for a,b in M if 0<=a<n and 0<=b<n}

n = int(input())
B = [[[] for _ in range(1,n)] for _ in range(1,n)]
for i,j in ((i,j) for i in range(1,n) for j in range(i,n)):
    moves = history = {(0,0)}; turn = 0
    while (n-1,n-1) not in moves:
        moves = set.union(*(next_moves(a,b,i,j,n)
                            for a,b in moves)) - history
        if not moves: turn = -1; break
        history |= moves; turn += 1
    B[i-1][j-1] = B[j-1][i-1] = turn;
for r in B: print(*r)