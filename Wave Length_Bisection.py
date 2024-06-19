print('Program to determine Wavelength of Ocean Wave')
import math
g=9.8
t=int(input("Enter the value of time period: "))
h=int(input("Enetr the depth: "))
def f(L):
    return ((g*(t**2)))/((2*math.pi))*(math.tanh(2*math.pi*h)/L)
def bisection(a,b,n):
    i=1
    condition=True
    while condition:
        L=(a+b)/2
        if f(L)<0:
            b=L
        else:
            a=L
        print('Iteration=',i,'L=',L,'f(L)=',f(L))
        if i==n:
            condition=False
        else:
            condition=True
            i=i+1
a=float(input("Enter first approximation root = "))
b=float(input("Enter 2nd approximation root = "))
n=int(input("Enter the no of iteration = "))
n=float(n)
if f(a)*f(b)>0:
    print('Try Again with different values')
else:
    bisection(a,b,n)
