import copy

def warshall_floyd(E:list,N:int):
    Ans = copy.deepcopy(E)
    for i in range(N + 1):
        Ans[i][i] = 0
    for k in range(1,N + 1):
        for i in range(1,N + 1):
            for j in range(1,N + 1):
                Ans[i][j] = min(Ans[i][j],Ans[i][k] + Ans[k][j])
    return Ans

