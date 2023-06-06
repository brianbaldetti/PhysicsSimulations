Web VPython 3.2

ball = sphere(radius=1, color=color.white)
ground = box(pos = vector (0, 0, 0), size = vector(100, 0.5 ,1), color = color.green)

v = 14          #initial velocity
g = -9.8         #gravitational acceleration
t = 0            #time
dt = 0.01        #as this decreases the accuracy increases

attach_trail(ball)    #allows us to trace ball


#loop runs until the ball starts impacting the gounrd
while ball.pos.y >= 0:
  rate(200)
  ball.pos.y += (v * dt)
  v += (g * dt)
  t += dt
  #code below also adds some horizontal deflection
  #ball.pos.x += dt
  
print("The time to hit the ground was: ", t, " seconds.")
