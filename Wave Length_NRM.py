print('Program to determine Wavelength of Ocean Wave')
import math as m
import matplotlib.pyplot as plt
g = 9.8
def f(l, T, h):
    res = l - ((g * T ** 2) / (2 * m.pi)) * (m.tanh((2 * m.pi * h) / l))
    return res
def df(l, T, h):
    res = 1 + ((g * T ** 2 * h) / l ** 2) * (1 / (m.cosh((2 * m.pi * h) / l) ** 2))
    return res
T = float(input('Enter Time Period in second '))
h = float(input('Enter the Depth of Ocean in meter '))
l = float(input('Enter Intial guess for Wavelength of Wave in meter '))
tol = 1e-15
i = 0
while i <= 100:
    L = l - (f(l, T, h) / df(l, T, h))
    if abs(L - l) < tol:
        break
    l = L
    print('Wavelenght is equal to', L, 'm at iteration', i)
    i=i+1

c=10
d=[]
while c<=300:
    d.append(c)6
    c=c+10



x=d
y=[36.56282787228761,38.87179264493567,38.98803364195473,38.992764479474296,38.9929532241217,38.992960745382355,38.99296104507708,38.99296105701879,38.99296105749462,38.992961057513575, 38.992961057514336,38.992961057514364,38.992961057514364, 38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364,38.992961057514364]
plt.plot(x,y)
plt.xlabel('Depth(m)')
plt.ylabel('Wavelenght(m)')
plt.title('Wavelength vs Depth')
plt.show()


