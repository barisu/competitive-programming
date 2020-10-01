from math import log2,ceil

class SegT:
    def __init__(self,num_factor:int):
        self.num_factor = num_factor
        self.length = 2*2**ceil(log2(num_factor)) - 1
        self.INT_MAX = 2**31 - 1
        self.tree = [self.INT_MAX]*self.length
        return

    def update(self,index,value):#0-indexed
        index += self.length // 2
        self.tree[index] = value
        while index > 0:
            index = (index - 1) // 2
            self.tree[index] = min(self.tree[index*2 + 1], self.tree[index*2 + 2]) 
        return

    def queryA(self,left: int, right: int , node : int, node_left :int, node_right :int)->int:#[left, right]
        if node_right < left or right < node_left:
            return self.INT_MAX
        elif left <= node_left and node_right <= right:
            return self.tree[node]
        tmp1 = self.queryA(left , right , node*2 + 1, node_left, (node_right + node_left) // 2)
        tmp2 = self.queryA(left , right , node*2 + 2, (node_right + node_left) // 2 + 1, node_right )
        return min(tmp1, tmp2)

    def query(self,left: int, right: int):
        return self.queryA(left,right,0,0,self.length // 2)


def main():
    seg = SegT(10)
    for i in range(10):
        seg.update(i,i**2)
    for i in range(10):
        for j in range(i,10,2):
            print(f"min between {i} and {j} is {seg.query(i,j)}")
    return

if __name__ == "__main__":
    main()

