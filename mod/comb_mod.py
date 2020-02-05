class Mod:
    fac = []
    inv = []
    finv = []
    mod = 0
    def __init__(self,maxi:int ,mod:int):
        self.mod = mod
        self.fac = [1]*maxi
        self.inv = [1]*maxi
        self.finv = [1]*maxi
        for i in range(2,maxi):
            self.fac[i] = self.fac[i - 1]*i%mod
            self.inv[i] = mod - self.inv[mod%i]*(mod//i)%mod
            self.finv[i] = self.finv[i-1]*self.inv[i]%mod


    def com(self,n:int, k:int)->int:
        #return nCk
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n]*(self.finv[k]*self.finv[n-k]%self.mod)%self.mod
