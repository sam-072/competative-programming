def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

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

if __name__ == '__main__':
    for _ in range(int(input())):
        a,b,d=map(int,input().split())
        g=gcd(a,b)
        # print("gcd=",g)
        a,b,d=a//g,b//g,d//g
        # print(a,b,d)
        if d%g!=0:
            print(0)
            continue
        if d==0:
            print(1)
            continue
        y1=((d%a)*modlo_inverse(b,a))%a
        if d<y1*b:
            print(0)
            continue
        n=(d//b-y1)//a
        print(n+1)

