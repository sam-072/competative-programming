def reduce_a(a,b):
    p=0
    for i in a:
        p=((p*10) + int(i))%b
    return p
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def advanced_gcd(a,b):
    num=reduce_a(a,b)
    return gcd(num,b)

if __name__ == '__main__':
    a=input()       #we assume that a is the largest number stored in string
    b=int(input())   # we assume that b is smaller number stored in int
    print(advanced_gcd(a,b))
