import heapq
def djikstra(node_num:int,E:list,start:int,distance:dict)->list:
    Ans = [float("inf")]*(node_num + 1)
    node = start
    Ans[start] = 0
    heap = []
    gone = [False]*(node_num + 1)
    gone[start] = True
    for i in range(node_num):
        for e in E[node]:
            if Ans[e] > distance[(node,e)] + Ans[node] and not(gone[e]):
                Ans[e] = Ans[node] + distance[(node,e)]
                heapq.heappush(heap,(Ans[e],e))
        while True:
            if len(heap) == 0:
                break
            dist,node = heapq.heappop(heap)
            if Ans[node] == dist:
                gone[node] = True
                break
    return Ans
