# The Dictionary Data Type
myCat = {'size':'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size'] # 'fat'
'My cat has ' + myCat['color'] + ' fur.'  # 'My cat has gray fur.'

# Dictionaries vs. List
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon # False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie' }
eggs == ham # True


# birthday.py
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True: 
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
        
    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        

# Odered dictionaries in Python 3.7
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
list(eggs) # ['name', 'species', 'age']
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie' }
list(ham) # ['species', 'age', 'name']


# The keys(), values(), and items() Methods
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
# red
# 42


for k in spam.key():
    print(k)
#color
#age

for i in spam.items():
    print(i)
# ('color': 'red')
# ('age': 42)  # Values in dict_items value returned by the items() method are tuples of the key and value.

# If you want a true list from one of these methods, see this example:
spam = {'color': 'red', 'age': 42}
spam.keys() # dict_keys(['color', 'age'])
list(spam.keys()) #['color', 'age']


spam = {'color': 'red', 'age': 42}
for k, v, in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
# Key: color Value: red
# Key: age Value: 42


# Checking Wether a Key or Value Exists in a Dictionary
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys() # True
'Zophie' in spam.values() # True
'color' not in spam.keys() # True
'color' in spam # False


# The get() Method
# has 2 arguments: the key of the value to retrieve and a fallback value to return if that key does not exist
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'


# The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam: 
    spam['color'] = 'black'
# same code with setdefault() method:
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')  # 'black'
spam #  {'color': 'black', 'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'white')  # 'black'
spam # {'color': 'black', 'name': 'Pooka', 'age': 5}


# CharacterCount.py
message = 'It was a bright cold day in April, and the clocks were strinking thirteen'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
    
print(count)


# Pretty Print
import pprint
message = 'It was a bright cold day in April, and the clocks were strinking thirteen'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
    
pprint.pprint(count)