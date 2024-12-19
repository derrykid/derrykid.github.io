#### Escape characters
| Escape character | Prints as    |
|------------------|--------------|
| \'               | Single quote |
| \"               | Double quote |
| \t               | Tab          |
| \n               | new line     |
| \\               | backslash    |

#### Raw strings
Raw string ignores all escape characters
```python
print(r'That is Carol\'s cat.')
That is Carol\'s cat.
```

#### Multiline strings with triple quotes
All between the triple quotes are considered part of the string.
```python
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```

Output
```
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
```

#### Indexing and slicing strings
Think of the string as a list, each char as an item

List
```python
foo = 'hello wolrd'
for i in range(len(foo)):
    print(foo[i])
```

Slice
```python
foo[-1] # d
```

#### `in` and `not in` with strings, contain method in Java
```python
'Hello' in 'Hello, World'   # True
'ho' not in 'hoho'      # False
```

#### String interpolation
```python
'My name is %s' $ (name)
# will substitue the %s with name variable
```

f-string
```python
>>> name = 'Al'
>>> age = 4000
>>> f'My name is {name}. Next year I will be {age + 1}.'
'My name is Al. Next year I will be 4001.'
```

#### Method

string letter, number related
- upper() - to upper case
- lower()
- isupper()
- islower()
- isalpha() - if all letters no blank
- isalnum() - if all letters, number, no blank
- isdecimal() - if all numberic character, no blank
- isspace() - if only space, tabs, new line
- istitle() - if start with Captial follow by lowercase

```python
'This Is Title Case'.istitle()  # True
```

startswith(), endswith()
```python
>>> 'Hello, world!'.startswith('Hello')
True
>>> 'Hello, world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
```

#### concatenate string method
It's kind of not intuitive. We'd expect like `list.join(', ')`, but it's not how it is in python
```python
newString = ', '.join(['cats', 'rats', 'bats'])
# 'cats, rats, bats'
```

#### Split the string

By default it's split whitespace characteres such as the space, tab, or newline characters are found.
```python
'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```

can pass the delimiter if desire
```python
'MyABCnameABCisABCSimon'.split('ABC')
# ['My', 'name', 'is', 'Simon']
```

**Common use are to split the multiline string** 
```python
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''

stringList = spam.split('\n')
```

##### Splitting with partition()
It'll split it into 3 parts: *before, separator, after.* It splits the first occurrence.
```python
>>> 'Hello, world!'.partition('w')
# ('Hello, ', 'w', 'orld!')
>>> 'Hello, world!'.partition('world')
# ('Hello, ', 'world', '!')
```

#### justify method
rjust()
```python
>>> 'Hello'.rjust(10)
'     Hello'
```

ljust()
```python
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
```

center
```python
>>> 'Hello'.center(20)
'       Hello        '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

#### remove space
Remove space, tab, newline
- strip() - strip space as default, otherwise specify the char to strip. e.g. strip('La')
- rstrip()
- lstrip()

```python
>>> spam = '    Hello, World    '
>>> spam.strip()
'Hello, World'
>>> spam.lstrip()
'Hello, World    '
>>> spam.rstrip()
'    Hello, World'
```

#### get the ascii code
return `int` type
```python
ord('A')
```
