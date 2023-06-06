Web VPython 3.2
from visual import *


 # Starting conditions (fill these in!)
x = 0
v = 0
a = 0.06
ts = 1.4   #the idle time
dt = 0.001  #as this gets smaller the numbers get more accurate
t = 0

f1=series(color=color.blue)

#idle time
while t < ts:
  f1.plot(t, x)
  t += dt

#runs after idel is done
while t < 4.4:
  t += dt
  x += (v * dt) + (0.5 * a * dt * dt)
  v += a * dt
  f1.plot(t, x)


print("The final speed is: ",v)
print("The final speed is: ", x)

""""
A)  Solving Using Kinematics:
    4.4 - 1.4 = 3 sec
    then using x = (v0 * t) + (0.5 * a * t^2) to get distance
    and using v = v0 + (a * t) to get velocity

    x = 0.27 m
    v = 0.18 m/s
    
B)  By filling in the code I get the results:
    v = 0.183
    x = 0.279075
  
C)  The reason we get the results we get is because computers perform discrete
    calculations not continous ones, therfore decreasing the change in time we
    will have more accurate results and vice versa.



"""
