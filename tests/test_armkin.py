from armkin import forward, inverse
import math
x,y=forward(1,1,0.5,0.7)
t1,t2=inverse(1,1,x,y)
x2,y2=forward(1,1,t1,t2)
assert abs(x-x2)<1e-9 and abs(y-y2)<1e-9
