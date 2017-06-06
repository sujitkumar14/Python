#simple calculator
from __future__ import division

print("Welcome in the world of Mathematics..")
print("options:")
print("1.Addition of two numbers")
print("2.substraction of two numbers")
print("3. Multiplication of two numbers")
print("4.Division of two numbers")
x = 1
while(x):
    c = int(raw_input("Please Enter your option..."))
    first = int(raw_input("Enter your first number "))
    sec = int(raw_input("Enter your second number "))
    if(c==1):
        print('your answer is {}'.format(first+sec))
    elif(c==2):
        print('your answer is {}'.format(first-sec))
    elif(c==3):
        print('your answer is {}'.format(first*sec))
    elif(c==4):
        print('your answer is {}'.format(first/sec))

    x = int(raw_input("do you want to continue: 1.yes 0.No "))
