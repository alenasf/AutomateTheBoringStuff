#Negative Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1] # elepant
spam[-3] # bat


# Getting a List from another List with Slices
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4] # ['cat', 'bat', 'rat', 'elephant']
spam[1:3] # ['bat', 'rat']
spam[0:-1] # ['cat', 'bat', 'rat']
spam[:2] # ['cat', 'bat']
spam[1:] # ['bat', 'rat', 'elephant']
spam[:] # ['cat', 'bat', 'rat', 'elephant']


# Getting a List's length with the len() Function
spam = ['cat', 'dog', 'moose']
len(spam) # 3


# Changing Values in a List with Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam # ['cat', 'aardvark', 'rat', 'elephant']
spam[2]=spam[1]
spam # ['cat', 'aardvark', 'aardvark', 'elephant']
spam[-1] = 12345
spam # ['cat', 'aardvark', 'aardvark', 12345]

# List Concatenation and List Replication
[1, 2, 3] + ['A', 'B', 'C']
# [1, 2, 3, 'A', 'B', 'C']

['X', 'Y', 'Z'] * 3
#['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
# [1, 2, 3, 'A', 'B', 'C']


# Removing Values From Lists with del Statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam  # ['cat', 'bat', 'elephant']
del spam[2]
spam # ['cat', 'bat']


# Using for Loops with Lists
for i in range(4):
    print(i)
    
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    
# The in and not in Operators
'howdy' in ['hello', 'hi', 'howdy', 'heyas'] # True
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam # False
'howdy' not in spam # False

# Type in a pet name and then check wether the name is in a list of pets
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
