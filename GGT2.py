def GGT(a,b):
    while a!= b:
        if a > b:
            a = a-b
        elif b > a:
            b = b-a
    return a

def GGT2(a,b):
    if a<b :
        a = b
    while b>0:
        q = a//b
        r = a%b
        a = q*b+r
        a = b
        b = r
    return a

print (GGT(150,50))
print (GGT2(150,50))
