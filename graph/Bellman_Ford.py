def Bellman_Ford(node_num:int,start:int,goal:int,VWC:list)->list:
    Ans = [float("inf")]*(node_num + 1)
    Ans[start] = 0        
    for _ in range(node_num-1):
        for v,w,c in VWC:
            Ans[w] = min(Ans[w], Ans[v] + c)
    Pre = list(Ans)
    for _ in range(node_num-1):
        for v,w,c in VWC:
            Ans[w] = min(Ans[w], Ans[v] + c)
    if Ans[goal] == Pre[goal]:#閉路判定
        return Ans[goal]
    else:
        return float("inf")
