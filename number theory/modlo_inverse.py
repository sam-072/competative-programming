def extended_gcd(a,b):
    if b==0:
        return a,1,0
    gcd,x1,y1=extended_gcd(b,a%b)
    x=y1
    y=x1-(a//b)*y1
    return gcd,x,y

def modlo_inverse(a,m):
    gcd,x,y=extended_gcd(a,m)
    # print(gcd,x,y)
    return x
    
print(modlo_inverse(5,17))