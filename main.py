import tkinter as TK
from turtle import Screen, Turtle 

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segment1 = Turtle(shape = "square")
segment1.color("white")

segment2 = Turtle(shape = "square")
segment2.color("white")
segment2.goto(-20, 0)

segment3 = Turtle(shape = "square")
segment3.color("white")
segment3.goto(-40, 0)







screen.exitonclick()