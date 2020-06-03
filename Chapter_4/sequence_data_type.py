# 
name = 'Zophie'
name[0] # 'Z'
name[-2] # 'i'
name[0:4] # 'Zoph'
'Zo' in name # True
'z' in name # False
'p' not in name # False
for i in name:
    print('***' + i + '***')
#***Z***
#***o***
#***p***
#***h***
#***i***
#***e***


# Mutable and Immutable Data Types
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name # 'Zophie a cat'
newName # 'Zophie the cat'

# the contents of eggs are replaced with a new list value
eggs = [1, 2, 3]
eggs = [4, 5, 6]
eggs # [4, 5, 6]

# modify the original list value in place
eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
eggs # [4, 5, 6]


# The Tuple Data Type
eggs = ('hello', 42, 0.5)
eggs[0] # 'hello'
eggs[1:3] # ( 42, 0.5)
len(eggs) # 3

type(('hello', )) # <class 'tuple'>
type(('hello')) # <class 'str'>


#Converting Types with list() and tuple() functions
tuple(['cat', 'dog', 5]) # ('cat', 'dog', 5)

list(('cat', 'dog', 5)) # ['cat', 'dog', 5]
list('hello') # ['h', 'e', 'l', 'l', 'o']


## References
# integers
spam = 42
cheese = spam
spam = 100
spam # 100
cheese # 42

#lists
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # The reference is being copied, not the list
cheese[1] = 'Hello'# This changes the list value.
spam # [0, 'Hello', 2, 3, 4, 5]
cheese # The cheese variable refers to the same list.
# [0, 'Hello', 2, 3, 4, 5]


#Identity and the id() Function
bacon = 'Hello'
id(bacon) # 140694618978864
bacon += ' world!' # A new string is made from 'Hello' and ' world!'
id(bacon) # bacon now refers to a completely different string. # 140694619023280


eggs = ['cat', 'dog'] # This creates a new list.
id(eggs) # 140694618441680
eggs.append('moose') # append() modifies the list "in place".
id(eggs) # eggs still refers to the same list as before. # 140694618441680
eggs = ['bat', 'rat', 'cow'] # This creates a new list, which has a new indentity.
id(eggs) # eggs now refers to a completely different list. # 140694618224352


# Passing References
def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1, 2, 3]
eggs(spam)
print(spam)
# [1, 2, 3, 'Hello']


# The copy Module's copy() and deepcopy() Function
import copy 
spam = ['A', 'B', 'C', 'D']
id(spam) # 140694617686816
cheese = copy.copy(spam)
id(cheese) # cheese is different list wih different indentity. # 140694618396144
cheese[1] = 42
spam # ['A', 'B', 'C', 'D']
cheese # ['A', 42, 'C', 'D']

