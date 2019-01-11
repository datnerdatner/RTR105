import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from matplotlib import pyplot as plt
from math import cos,sin

x=[]
y=[]
y2=[]
for i in range (70):
	x.append(i/10.)
	y.append(cos(x[i]))
	y2.append(sin(x[i]))

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$ un $sin(x)$')
plt.plot(x,y, color = "#ff69b4")
plt.plot(x,y2, color = "#7FFF00")
plt.show()
