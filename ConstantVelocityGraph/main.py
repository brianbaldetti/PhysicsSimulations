Web VPython 3.2
from visual import *

x = -0.5
t = 0
v = 0.45
dt = 0.1

tgraph = graph(xtitle="Time [s]", ytitle="Position [m]")
f1 = gcurve(color=color.blue)

#while loop that updates variables
while t < 1.5:
   x = x + v*dt       #updates position
   t += dt            #updates time
   f1.plot(t,x)

#prints output
print("The final position is", x)

"""""
A) No you don't need to include in your variables,
   however all the variables have to be the same type and same prefix.
   
B) 
    1. The cart will be at 0.99 meters at 2.2 seconds.
    2. The cart will be at 0.93 meters at 1.5 seconds.
    3. The cart will be at 0.175 meters at 1.5 seconds.
    
C) Because we change the value of X. We could use a X0 value if we want;
   however, there would not be any advantage and we would have to use
   xtra code and instruction.

"""
