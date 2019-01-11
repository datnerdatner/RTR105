# 191.py Sagatave datu ierakstam failaa
# Autors: Renats Jakubovskis
# Datums: 09.12.2018
from math import sin

def f(x):
    return sin(x)
	
h=0.01
a=0
	
datu_fails = open("92.dat", "w")

for i in range (330):
    f0 = float((f(a+h) - f(a))/h)
    f1 = float((f(a+2*h) - f(a+h))/h)
    f2 = (f1-f0)/h
    datu_fails.write("%.2f\t%f\t%f\t%f\n" % (a,sin(a),f0,f2))
    a += h
datu_fails.close()
