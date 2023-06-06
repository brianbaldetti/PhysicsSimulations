Web VPython 3.2
ground = box(pos = vector (0, 0, 0), size = vector(100, 0.2,1), color = color.green)
ball = sphere(pos = vector(-4.5, 0, 0), radius = 0.2, color = color.yellow)

g = vector(0, -9.8, 0)
v0 = 120
theta = 45 * pi / 189

ball.m = 0.5
ball.v = v0 * vector(cos(theta), sin(theta), 0)
ball.p = ball.m * ball.v
c = 0.7
rho = 1.2
A = pi * ball.radius **2


t = 0
dt = 0.01

attach_trail(ball)

while ball.pos.y >= 0:
  rate(200)
  F = ball.m * g - 0.5 * rho * A * c * mag(ball.p/ball.m) ** 2 * norm(ball.p)
  ball.p += F * dt
  ball.pos += ball.p * dt / ball.m
  t += dt

  print("the final position is ", ball.pos)
