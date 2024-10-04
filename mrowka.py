import math

#4.1
r = 5
T = 12.5
dt = 0.05
t = 3
x = [0]
y = [0]
i = 0

while(x[i]>=y[i]):
    t += 0.05
    i += 1
    x.append(r*math.sin(2*math.pi*t/T))
    y.append(r*math.cos(2*math.pi*t/T))
print(t)

#4.2
t=0
x=[]
y=[]
dt = 0.5
T = 10
while(t<=10):
    r=t
    x.append(r*math.sin(2*math.pi*t/T))
    y.append(r*math.cos(2*math.pi*t/T))
    t+=0.5

