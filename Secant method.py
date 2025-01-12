x1=6
x2=4
total=0.5
num_iter=20
def func(p):
    return p*p*p-p*p+p-5
for i in range(1,num_iter,1):
    f_x1=func(x1)
    f_x2=func(x2)
    print(str(i)+'x:'+str(x2)+'f(x)'+str(f_x2))
    if abs(f_x2)<total:
        break
    x3=x2-f_x2*((x2-x1)/(f_x2-f_x1))
    x1=x2
    x2=x3
print('Your"zero" is located at :['+str(x2)+','+str(f_x2)+']')