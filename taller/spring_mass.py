from vpython import *


mass=box(pos=vector(12,0,0),velocity=vector(0,0,0),size=vector(1,1,1), mass=1.0,color=color.blue)
k=1
pivot=vector(0,0,0)
spring=helix(pos=pivot, axis=mass.pos-pivot, radius=0.4, constant=k,thickness=0.1, coils=20, color=color.red)

eq=vector(9,0,0)
t=0
dt=0.01
while (t<50):
  rate(100)
  acc=(eq-mass.pos)*(spring.constant/mass.mass)
  mass.velocity=mass.velocity+acc*dt
  mass.pos=mass.pos+mass.velocity*dt
  spring.axis=mass.pos-spring.pos
  t=t+dt
  print(mass.pos.x,t)