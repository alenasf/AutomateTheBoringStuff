# Escape Characters
# \' - Single quote
# \" - Double quote
# \t - Tab
# \n - Newline(line break)
# \\ - Backslash 

print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings
print(r'That is Carol\'s cat.')


# Multiple Strings with Triple Quotes
print(''' Dear Alice, 

Eve's cat has been arrested for catnapping.

Sincerely, 
Bob
''')

print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping.\n\nSincerely,\nBob)
      
      
# Indexing and Slicing Strings
spam = 'Hello, world!'
spam[0] # 'H'
spam[4] # 'O'
spam[-1] # '!'
spam[0:5] # 'Hello'
spam[:5] # 'Hello'
spam[7:] # 'world!'

# slicing does not modify the original string.
spam = 'Hello, world!'
fizz = spam[0:5]
fizz => 'Hello'
     
      
# The in and not in Operators with Strings
'Hello' in 'Hello, World!' # True
'Hello' in 'Hello' # True
'HELLO' in 'Hello, World!' # False
'' in 'spam' # True
' ' in 'spam' # False
'cats' not in 'cats and dogs' # False
      
      
# Putting Strings Inside Other Strings
name = 'AI'
age = 4000
'Hello, my name is ' + name + '. I am ' + str(age) + 'years old.'
# 'Hello, my name is AI. I am 4000years old.'
      
# string interpolation
name = 'AI'
age = 4000
'My name is %s. I am %s years old.' % (name, age)
# 'My name is AI. I am 4000 years old.'
      
#f-strings
name = 'AI'
age = 4000
f'My name is {name}.Next year i will be {age + 1}.'
# 'My name is AI.Next year i will be 4001.'
      
      
      
      
    