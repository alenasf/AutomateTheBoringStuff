# The upper(), lower(), isupper(), and islower() Methods
spam = 'Hello, world!'
spam = spam.upper()
spam # 'HELLO, WORLD!'
spam = spam.lower()
spam # 'hello, world!'


print("How are you?")
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:  
    print('I hope the rest of your day is good')
    
    
spam = 'Hello, world!'
spam.islower() # False
spam.isupper() # False
'Hello'.isupper() # True
'abc12345'.islower() #True
'12345'.islower() # False
'12345'.isupper() # False


# upper() and lower() string methods themselves return string.
'Hello'.upper() # 'HELLO'
'Hello'.upper().lower() # 'hello'
'Hello'.upper().lower().upper() # 'HELLO'
'HELLO'.lower() # 'hello'
'HELLO'.lower().islower() # True


# The isX() Methods
'hello'.isalpha() # True
'helo123'.isalpha() # False
'hello123'.isalnum() # False
'hello'.isalnum() # True
'123'.isdecimal() # True
'  '.isspace() # True
'This Is Title Case'.istitle() # True
'This Is Title Case 123'.istitle() # True
'This Is NOT Title Case Either'.istitle() # False

#ValidateInput.py
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
    
while True: 
    print('Select a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
    
    
# The startswith() and endswith() Methods
'Hello, world!'.startswith('Hello') # True
'Hello, world!'.endswith('world!') # True
'abc123'.stratswith('abcdef') # False
'abc123'.endswith('12') # False
'Hello, world!'.startswith('Hello, world!') # True
'Hello, world!'.endswith('Hello, world!') # True


# The join() and split() Methods
', '.join(['cats', 'rats', 'bats'])
# 'cats', 'rats', 'bats'
' '.join(['My', 'name', 'is', 'Simon'])
#'My name is Simon'
'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimonABC'


# the split() method
'My name is Simon'.split()
['My', 'name', 'is', 'Simon']

'MyABCnameABCisABCSimonABC'.split('ABC')
['My', 'name', 'is', 'Simon']

'My name is Simon'.split('m')
['My na', 'e is Si', 'on' ]

# split a multiplestring along the newline character.
spam = ''' Dear Alice, 
How have you been? I am fine.
There is a container in the fridge
that is labled "Milk Experiment."

Please do not drink it.
Sincerely, 
Bob
'''

spam.split('\n')
# result
[' Dear Alice, ',
 'How have you been? I am fine.',
 'There is a container in the fridge',
 'that is labled "Milk Experiment."',
 '',
 'Please do not drink it.',
 'Sincerely, ',
 'Bob',
 '']

# Justifying Text with the rjust(), ljust(), and center() Methods
'Hello'.rjust(10)
# '       Hello'
'Hello'.rjust(20)
# '     Hello'
'Hello, world'.rjust(20)
#'       Hello, world'
'Hello'.ljust(10)
#'Hello      '

'Hello'.rjust(20, '*')
# '***************Hello'
'Hello'.ljust(20, '-')
# 'Hello---------------'

'Hello'.center(20)
#'       Hello        '
'Hello'.center(20, '=')
#'=======Hello========'


# picnicTable.py
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '-') + str(v).rjust(rightWidth))
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# ---PICNIC ITEMS--
# sandwiches--    4
# apples------   12
# cups--------    4
# cookies----- 8000
# -------PICNIC ITEMS-------
# sandwiches----------     4
# apples--------------    12
# cups----------------     4
# cookies-------------  8000


# Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
spam = '     Hello, world    ' 
spam.strip()
#'Hello, world'
spam.lstrip()
#'Hello, world   '
spam.rstrip()
#'   Hello, world'

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')

# Copying and Pasting Strings with the pyperclip Module
import pyperclip

pyperclip.copy('Hello, world')
pyperclip.paste()
# 'Hello, world!'







