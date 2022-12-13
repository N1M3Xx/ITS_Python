import pygame
import time
import random

green = (0, 255, 0)

dis_width = 800
dis_height = 800
block = 200
 
x = []
y = []
c = []

for ct in range(1):
    x.append(round(random.randrange(0, dis_width - block) / 200.0) * 200.0)
    y.append(round(random.randrange(0, dis_height - block) / 200.0) * 200.0)
    c.append(green)
    
print(x)
print(y)
print(c)
print("\n\n")

for i in range(len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                y[j], y[j + 1] = y[j + 1], y[j]
                c[j], c[j + 1] = c[j + 1], c[j]
    
print(x)
print(y)
print(c)