 # Return Values and return Statements
    
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4: 
        return 'Reply hazy try again'
    elif  answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
# or print(getAnswer(random.randint(1, 9)))


# Local and Global Scope

# Local Scopes Cannot Use Variable in Other Local Scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0
    
spam()
    

# Global Variables Can Be Read From a Local Scope
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)


# Local and Global Variables with the Same Name
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs)  # prints 'bacon local'
    
eggs = 'global'
bacon()
print(eggs)  # prints 'global'


# The global Statement
def spam():
    global eggs
    eggs = 'spam' # this is the global
    
def bacon():
    eggs = 'bacon' # this is a local
    
def ham():
    print(eggs) # this is a global
    
eggs = 42 # tihs is a global 
spam()
print(eggs)


# The global Statement
def spam():
    global eggs
    eggs = 'spam'
    eggs = 'global'
    spam()
    print(eggs)
    
    
# Exception Handling 1
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


# Exception Handling 2
def spam(divideBy):
    return 42 / divideBy

try: 
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
