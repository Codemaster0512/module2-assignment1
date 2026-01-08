#Perform Basic Mathematical Operations
#Takes two numbers as input from the user.

a=int(input('Enter a first number: '))
b=int(input('Enter a second number: '))

#Performs the basic mathematical operations on these two numbers:

A=a+b       #Addition
S=a-b       #Subtraction
M=a*b       #Multiplication
D=a/b       #Division

#Displays the results of each operation on the screen.

print('Addition', A)
print('Subtraction', S)
print('Multiplication', M)
if b=!=0:
    print('Division', D)
else:
    print('Division by zero is not possible')