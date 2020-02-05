class UnionFind:
    UF = []
    def __init__(self,N:int):
        self.UF = list(range(N + 1))
        return

    def getParent(self,index:int)->int:
        if self.UF[index] == index:
            return index
        else:   
            self.UF[index] = self.getParent(self.UF[index])
            return self.UF[index]

    def join(self,parent:int,child:int):
        boss = self.getParent(parent)
        self.UF[child] = boss
        return
        

