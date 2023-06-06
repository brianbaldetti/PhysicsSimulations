Web VPython 3.2
from visual import *

#initialized values
A = vector(1, 2, 3)
B = vector(-2, 0, 1)

#trials ran
print(A+B)
print(A.y)
print(1.5*B)
print(mag(B))
print(hat(A))
print(dot(A,B))


""""
A) A + B = -1, 2, 4

B) A.y = 2

C) 1.5 * B = -3, 0, 1.5

D) mag(B) = sqrt(5)

E) hat(A) = sqrt(15)
  ACTUAL: < 0.267261, 0.534522, 0.801784 >

F) dot(A, B) = -2, 0, 3
  ACTUAL: 1


"""
