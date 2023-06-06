Web VPython 3.2

""""
2)
    The initial velocity of the satellite is 0.
    
    dt is set to such a high number b/c otherwise the motion of 
  the motion of the satellite would be too slow to observe.
  
    The while loop terminates when the satellite makes contact 
  with the earth.
  
    The earth should not be programmed to move b/c the gravitational force
  acts upon the earths center of mass.
  
2)
  The satellite moves in an an eliptical orbit around the earth
  
3) 
  The minimum speed I was able to find was 3300 for the tangental velocity,
this suprised be b/c I calculated the velocity needed to be ~4500m/s, so
I don't know why this value is so low.

4)
  The max speed was 6400 after that the satellite would never return, 
though I guess thought that as time went to infinity it would still
theortically return because the gravity never actually reaches 0.
"""

#initializing values for the energy vs distance graph
energy_graph=graph(ytitle="Energy [J]", 
  xtitle="Distance [m]", 
  title="Energy Graph #1")
kCurve = gcurve(graph=energy_graph, color=color.red)
uCurve = gcurve(graph=energy_graph, color=color.blue)
eCurve = gcurve(graph=energy_graph, color=color.green)

#initializingn values for the energy vs. time graph
time_graph=graph(ytitle="Energy [J]", 
  xtitle="Time [s]", 
  title="\n\n\nEnergy Graph# 2")
kCurve2 = gcurve(graph=time_graph, color=color.red)
uCurve2 = gcurve(graph=time_graph, color=color.blue)
eCurve2 = gcurve(graph=time_graph, color=color.green)

#initialized constants
G = 6.68e-11
M_E = 5.97e24
R_E = 6.4e6

#initialized objects
Earth=sphere(pos=vec(0,0,0), radius=R_E, texture=textures.earth)
ball = sphere(pos=vector(3*R_E, 0, 0), radius=R_E/100)

#initialized variables for mass, velocity, and momentum
Earth.m = M_E
ball.m = 1
#max was ~6400 min was ~3300
ball.p = ball.m * vector(0,0,4000)
attach_trail(ball)


#time variables
t = 0
dt = 60

#loops runs while the ball does not make contact with the earth
while mag(ball.pos) > R_E:
  rate(60)
  #radius of orbit
  r = ball.pos - Earth.pos
  #force of gravity
  F = (-G * M_E * ball.m) * norm(r) / (mag(r)**2)
  ball.p = ball.p + F * dt
  ball.pos = ball.pos + ball.p * dt / ball.m
  
  #kinetic energy and potential energy calc
  kE = 0.5 * ball.m * (mag(ball.p)/ball.m)**2
  uE = (-G * ball.m * M_E) / mag(r)
  
  """
  testing code
  print(mag(r))
  print(ball.p)
  """
  
  #outputs values to graphs
  kCurve.plot(mag(r), kE)
  uCurve.plot(mag(r), uE)
  eCurve.plot(mag(r), (kE-uE))
  
  kCurve2.plot(t, kE)
  uCurve2.plot(t, uE)
  eCurve2.plot(t, (kE-uE))
  
  #updates time
  t = t + dt
