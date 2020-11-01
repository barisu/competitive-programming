class UnionFind:
    UF = []
    def __init__(self,N:int):
        self.N = N
        self.UF = list(range(N + 1))
        return

    def getParent(self,index:int)->int:
        if self.UF[index] == index:
            return index
        else:   
            self.UF[index] = self.getParent(self.UF[index])
            return self.UF[index]

    def join(self,parent:int,child:int):
        root = min(self.getParent(parent),self.getParent(child))
        self.UF[child] = root
        self.UF[parent] = root
        return
    
    def size(self,n:int)->int:
        
        for i in range(self.N):
            self.getParent(i)
        return self.UF.count(self.getParent(n))
