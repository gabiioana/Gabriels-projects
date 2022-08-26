#This is my first python project. It's a function that turns any string into a rainbow!!

import sys
from termcolor import colored, cprint
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
def rainbify(x):
    for i, letter in enumerate(x):
        cprint(letter, colors[i % len(colors)], end="")

rainbify('This is the best function anyone can ever make in python')
rainbify('Tritan cups are not the best cups for there is a cup thatis better than tritan cups')