from matplotlib import pyplot as plt
from math import sin,factorial

x=[]
y=[]
f1=[]
f2=[]
f3=[]
f4=[]

for i in range(71):
    x.append(i/10.)
    f1.append(x[i])
    f2.append(f1[i] - x[i]**3/factorial(3))
    f3.append(f2[i] + x[i]**5/factorial(5))
    f4.append(f3[i] - x[i]**7/factorial(7))
    y.append(sin(x[i]))

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.ylim(-2,2)
plt.plot(x,y, color = "#B0171F")
plt.plot(x,f1, color = "#8B4789")
plt.plot(x,f2, color = "#473C8B")
plt.plot(x,f3, color = "#00CED1")
plt.plot(x,f4, color = "#308014")
plt.show()
