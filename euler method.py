def f(x,y):
    return eval(function)


function=input("enter the function:")
xi,yi,finalx,h=float(input("enter initial value of x:")),float(input("enter initial vlaue of y:")),float(input("enter final value of x:")),float(input("enter step length:"))
count=0
print(f"{count}  y({round(xi,1)})={round(yi,4)}")
while xi<finalx:
    yi=yi+h*f(xi,yi)
    xi=xi+h
    count=count+1
    print(f"{count}  y({round(xi,1)})={round(yi,4)}") 
   
