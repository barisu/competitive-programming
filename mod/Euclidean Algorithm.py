
def euclid(a:int,b:int)->(int,int):
    #return x,y s.t ax + by = gcd(a,b)
    #a > b >= 0
    if b == 0:
        return 1,0
    x,y = euclid(b,a%b)
    return y,x - y*(a // b)

def inverse(a:int,mod:int)->int:
    #gcd(p,b) == 1
    if mod > a:
        n,x = euclid(mod,a)
    else:
        x,n = euclid(a,mod)
    return x

def devide_mod(a:int,b:int,mod:int)->int:
    #a // b
    x = inverse(b,mod)
    return  (a*x)%mod

