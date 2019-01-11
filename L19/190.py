from math import sin

def f(x):
    return sin(x)

h=0.01 ; a=0

for i in range (330):
    f1 = float((f(a + h) - f(a))/h)
    print a,f(a),f1
    a += h
