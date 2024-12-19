"""Multi-line comments
Works
"""

print('''
This can work with double quotes as well
''')

# String interpolation
name = 'Al'
age = 4000
print("My name is %s. I'm %s years old." % (name, age))

# f string
print(f'My name is {name}. Next year I will be {age + 1}')

# isX() methods
spam = "hello"
spam.isalpha()
spam.isalnum()
spam.isalnum()
spam.isdecimal()
spam.isspace()
spam.istitle()

# join(), split()
' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'.split() # default is whitespace

# partition(), divided into 3 parts
'Hello, world!'.partition('w') # divide by 'w'
# alternatively
before, sep, after = 'Hello, world!'.partition(' ')

# rjust(), ljust(), center()
'Hello'.rjust(20, '*')
# '***************Hello'
'Hello'.ljust(20, '-')
# 'Hello---------------'
'Hello'.center(20, '=')
# '=======Hello========'


# remove whitespace
'  Hello  '.strip()
'  Hello  '.lstrip()
'  Hello  '.rstrip()

# join()
', '.join(['cats', 'rats','bats'])
# 'cats, rats, bats'