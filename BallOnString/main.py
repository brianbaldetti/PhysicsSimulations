Web VPython 3.2
""""
  4) Yes generate purly circular motion as shown on line 45,
  and linear motion as shown on line 48.
  
  5) K compresses the period as it increases and vice versa makes
  the motion more linear and spikey
     L0 increases the size of the orbit and starting energy if the initial
  position is not adjusted
     m increases the size of the orbit and speed as its energy is greater

"""





#initialized variables
t = 0
dt = 0.05
#orbits get more "spikey" and fast as k increases 
#k seems to compress the periods of the motion
k = 2
#periods get larger as L0 increases and smaller as it decreases
#just like as k, however if we also adjust the starting position
#accordingly it has a lesser effect
L0 = 0.16


table = box(
  pos=vec(0,0,-0.025), 
  size=vector(1, 1, 0.05), 
  color=color.green
  )
  
centralPost = cylinder(
  pos=vec(0,0,0.0),
  radius=0.01,
  axis=vector(0,0,0.05),
  color=color.red
  )
  
movingObj = sphere(
  pos=vec(0.1,0.1,0),
  radius=0.01,
  color=color.blue)
  

  
#orbits get larger as mass gets larger
#due to greater momentim and kinetic energy
movingObj.m = .2
# code below generates circular motion
movingObj.p = movingObj.m * vector(-1, 1,0)

# code here generates purely linear motion
# this is because obj has no motion in any other dimensions
#movingObj.p = movingObj.m * vector(0,0,0)

#code here generates a basic motion
#movingObj.p = movingObj.m * vector(1,0,0)
  
spring = helix(
  pos=centralPost.pos,
  radius=0.01,
  axis=movingObj.pos - centralPost.pos,
  color=color.green)
  
attach_trail(movingObj)  
  

while (t < 100):
  rate(100)
  
  #calculates length of string
  L = movingObj.pos - centralPost.pos
  
  #calculates spring force
  Fs = -k * (mag(L) - L0) * norm(L)

  #calcualtes objs momentum and position
  movingObj.p = movingObj.p + Fs * dt
  movingObj.pos = movingObj.pos + movingObj.p * dt / movingObj.m
  
  #updates spring
  spring.axis = movingObj.pos - centralPost.pos
  
  #updates time
  t += dt
