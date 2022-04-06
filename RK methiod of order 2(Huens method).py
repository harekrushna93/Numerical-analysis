from typing import Counter


def f (x,y):
    return eval(function)
function=input('enter function:')
xi,yi,finalx,h=float(input("Enter initial value of x: ")),float(input("Enter initial value of y: ")),float(input("Enter final value of x: ")),float(input("Enter step length: "))

count=0
while(xi<finalx):
    print(count,"  x{}={}   y{}={}".format(count,round(xi,1),count,round(yi,3)))
    count+=1
    k1=h*f(xi,yi)
    k2=h*f(xi+h,yi+k1)
    print("k1= ",round(k1,3))
    print("k2=",round(k2,3))
    yi=yi+(0.5)*(k1+k2)
    xi=xi+h
print(count,"  x{}={}   y{}={}".format(count,round(xi,1),count,round(yi,3)))