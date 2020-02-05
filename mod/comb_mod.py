mod  =10**9 + 7

def com_init(mx:int ,mod:int)->list:
    fac = [1]*mx
    inv = [1]*mx
    finv = [1]*mx
    for i in range(2,mx):
        fac[i] = fac[i - 1]*i%mod
        inv[i] = mod - inv[mod%i]*(mod//i)%mod
        finv[i] = finv[i-1]*inv[i]%mod
    return fac,finv,inv

fac,finv,inv = com_init(10**5,10**9 + 7)

def com(n:int, k:int):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n]*(finv[k]*finv[n-k]%mod)%mod

n,m = map(int,input().split())
print(com(n,m))