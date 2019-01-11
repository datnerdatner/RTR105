from matplotlib.pyplot import figure, show, suptitle
from math import pi
from cmath import *

fig = figure(0)
fig.suptitle('skaitli')
ax = fig.add_subplot(111, polar=True)
theta = [30,60]
theta = [i*pi/180 for i in theta]
r = [1.,2.]
ax.bar(theta,r, width=0.01) 

a=rect(r[0],theta[0])
b=rect(r[1],theta[1])

summa = a + b
starp = a - b
reiz = a * b
dali = a / b

r1 = abs(summa), abs(starp), abs(reiz), abs(dali)
theta1 = phase(summa), phase(starp), phase(reiz), phase(dali)

for i in range (4):
    fig = figure(i+2)
    ax = fig.add_subplot(111, polar=True)
    if i == 0:
        fig.suptitle('summa')
    if i == 1:
        fig.suptitle('starpiba')
    if i == 2:
        fig.suptitle('reizinajums')
    if i == 3:
        fig.suptitle('dalijums')
    ax.bar(theta1[i],r1[i], width=0.01)
show()
