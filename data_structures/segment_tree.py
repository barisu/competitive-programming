from math import log2,ceil

num_factor,num_query = map(int,input().split())
INT_MAX = 2**31 - 1 
length = 2*2**ceil(log2(num_factor)) - 1
tree = [INT_MAX]*length
Ans = []

def update(index,value):#0-indexed
    index += length // 2
    tree[index] = value
    while index > 0:
        index = (index - 1) // 2
        tree[index] = min(tree[index*2 + 1], tree[index*2 + 2]) 
    return

def query(left: int, right: int , node : int, node_left :int, node_right :int)->int:#[left, right]
    if node_right < left or right < node_left:
        return INT_MAX
    elif left <= node_left and node_right <= right:
        return tree[node]
    tmp1 = query(left , right , node*2 + 1, node_left, (node_right + node_left) // 2)
    tmp2 = query(left , right , node*2 + 2, (node_right + node_left) // 2 + 1, node_right )
    return min(tmp1, tmp2)


def main():
    for _ in range(num_query):
        com,x,y = map(int,input().split())
        if com:
            Ans.append(query(x,y,0,0,length // 2))
        else:
            update(x,y)
    print(*Ans, sep ="\n")
    return

if __name__ == "__main__":
    main()

