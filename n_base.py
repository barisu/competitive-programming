def n_number(num:int , n:int)->list:
    #n進数に直す
    ans = []
    while num > 0:
        ans.append(num%n)
        num = num // n
    return ans[::-1]
