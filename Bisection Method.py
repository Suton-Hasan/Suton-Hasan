def func(p):
    return p*p*p-p*p+2

def BisectionMethod(a,b):
    if(func(a)*func(b)>=0):
        print("Give your correct value")
        return
    c=a
    while((b-a)>=0):
        c=(a+b)/2
        if(func(c)==0):
            break
        elif(func(c)*func(a)<0):
            b=c
        else :
            a=c

    print("Root is:",c)

BisectionMethod(-200,300)
