'''
from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) <1:
          break
end_fill()
'''


import turtle   
spiral=turtle.Turtle()
for i in range(20):
      spiral.forward(i*15)
      spiral.right(144)
turtle.done()

