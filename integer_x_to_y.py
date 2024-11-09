'''
desc: display a series of numbers from x to y
author: vermilion10
date: November 2024
'''
x = int(input('input first number: '))
y = int(input('input second number: '))
for i in range(x, y+1):
    print(i, end=' ')
    i += 1
