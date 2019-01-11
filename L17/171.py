# Fails:170.py
# Autors: Renats Jakubovskis
# Apliecibas numurs: 181REB261
# Datums: 09.12.2018
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding: utf -8 -*-
from math import sin , fabs
from time import sleep
def f(x):
    return sin(x)

# Definejam argumenta x robezhas :
a = 1.1
b = 3.2

# Aprekjinam funkcijas vertibas dotajos punktos :
funa = f(a)
funb = f(b)

# Paarbaudam , vai dotajaa intervaalaa ir saknes :
if ( funa * funb > 0.0 ):
    print "Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit() # Zinjo uz ekraana , gaida 1 sec . un darbu pabeidz

# Defineejam precizitaati , ar kaadu mekleesim sakni :
deltax = 0.0001

# Sashaurinam saknes mekleeshanas robezhas :
k=0
while ( fabs(b-a) > deltax ):
    k+=1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x

print 'x = %f; f(x) = %f; k = %d' % (x,f(x),k)
