Web VPython 3.2
from visual import *

# Make two graphs - one for the police, one for the speeder
fp = gcurve(color=color.blue) # Police
fs = gcurve(color=color.red) # Speeder

# Initial conditions
xp = 0
xs = 0
vs = 40
vp = 0
vp_max = 60 # Max speed of police

# Acceleration of police
ap = 0 # Initialize
ap_acc = 6 # Value when accelerating

t = 0
dt = 0.01

# Time to wait for police to start
t_wait = 3

#idle time
while t < t_wait:
  xs += vs * dt
  t += dt
  
#police car catching up
while xp < xs:
  
  #if the car hasn't reached max velocity then it continues to speed up
  if vp < vp_max:
    vp += ap_acc * dt
  
  xs += vs * dt
  xp += vp * dt
  
  t += dt
  
print("The position of the cars when they catch up is: ", xp, " meters.")
print("It takes ", t, " seconds for the police car to catch up.")
print("The police car reaches max speed of: ", vp, "m/s.")
