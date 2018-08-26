

#2 –Take the user first name and last name and print it in reversed form

firstName = input('Input yout First Name')
lastName  = input('Input your last Name')

print(lastName + firstName)

# 2.–Take two numbers from user and perform arithmetic operations on them.

Number1 = float(input('Please add your first number: '))

Number2 = float(input('Please enter your second number: '))

add=Number1 + Number2

print(add)

substraction = Number1-Number2
print(substraction)

# 3.  Write a program that accepts a sentence and prints the number of letters anddigits in Sentence.

set = input('Please input a string')
d=l=0
for c in set:
    if c.isdigit():
        d=d+1
    elif c.isalphat():
        l=l+1
    else:
        pass
print("Number of letters",l)
print("Number of digits", d)



