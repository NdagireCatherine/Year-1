#number_15
x1=int(input("Enter 1st x-coordinate:"))
y1=int(input("Enter 1nd y-coordinate:"))
x2=int(input("Enter 2nd x-coordinate:"))
y2=int(input("Enter 2nd y-coordinate:"))
x=(1/2)*(x1+x2)
y=(1/2)*(y1+y2)
M=(x,y)
print(f"So the midpoint of the points ({x1};{y1}) and({x2};{y2}) is {M}")


#number_16
xx1=int(input("Enter 1st x-coordinate:"))
yy1=int(input("Enter 1st y-coordinate:"))
xx2=int(input("Enter 2st x-coordinate:"))
yy2=int(input("Enter 2nd y-coordinate:"))
xx=xx2-xx1
yy=yy2-yy1
Gradient=yy/xx
print(f"The gradient of the points ({xx1},{yy1}) and ({xx2},{yy2}) is {Gradient}.")


#number_17
xn=int(input("Enter the value of x:"))
x4=xn*xn*xn*xn
x3=xn*xn*xn
x2=xn*xn
x0=(xn+1)**2
rq=xn**(1/2)
N=(x4-x3+x2-xn)/(x0-rq)
print(f"Value of N ={N}")


#number_18

