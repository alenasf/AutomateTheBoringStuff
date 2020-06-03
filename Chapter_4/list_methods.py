# Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') # 0
spam.index('heays')

# Adding Values to Lists with the append() and insert() Methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam  # ['cat', 'dog', 'bat', 'moose']

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam # ['cat', 'chicken', 'dog', 'bat']


# Removing Values from Lists with the remove() Method
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')


# Sorting the Values in a List with the sort() Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam # [-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam # ['ants', 'badgers','cats', 'dogs', 'elephants']

spam.sort(reverse=True)
spam # ['elephants', 'dogs', 'cats', 'badgers', 'ants']


spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam # ['a', 'A', 'z', 'Z']


# Reversing the Values in a List with the reverse() Method
spam = ['cat', 'dog', 'moose']
spam.reverse()
spam # ['moose', 'dog', 'cat']