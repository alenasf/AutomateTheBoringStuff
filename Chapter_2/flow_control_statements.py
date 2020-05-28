# Flow Control Statements

# If Statements
if name == 'Alice':
    print('Hi, Alice!')
    
# else Statements 
if name == 'Alice':
    print('Hi, Alice!')
else: 
    print('Hello, stranger')
    
#elif Statements
if name == 'Alice':
    print('Hi, Alice')
elif age > 12:
    print('You are not Alice, kiddo.')

    
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print(You are not Alice, kiddo)
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alice, grannie.')

    
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo')
else:
    print('You are neither Alice not a little kid')
    
    
# while Loop Statements

spam = 0
if spam < 5:
    print('Hello, world')
    spam = spam + 1
    # here is the code with a while statement:
spam = 0
while spam < 5:
    print('Hello, world')
    spam = spam + 1
    
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you!')


# Break Statements
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')


# Continue Statements
while True:
    print('Who are you ?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe.What is the password?')
    password = input()
    if password == 'swordfish':
        break
print('Acess granted')


# for Loops and the range() Function
print('My name is')
for i in range(5):
    print('Jimmy Five Times(' + str(i) + ')')
    
total = 0
for num in range(101):
    total = total + num
print(total)


# Equivalent while Loop

print('My name is')
i = 0
while 1 < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
    
# random module

import random
for i in range(5):
    print(random.randint(1,10))
    
    
# sys.exit() Function
import sys

while True: 
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')