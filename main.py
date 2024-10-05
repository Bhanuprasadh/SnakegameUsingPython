import tkinter as TK
from turtle import Screen, Turtle 

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("balck")
screen.title("My Snake Game")

segment1 = Turtle(shape = "square")
segment1.color("white")

segment2 = Turtle(shape = "square")
segment2.color("white")

segment3 = Turtle(shape = "square")
segment3.color("white")







screen.exitonclick()