# About

This cheat sheet only contains the basic of Python in point of view of Java developer.

## Data types

get data type by `type()` function

```python
x = 5
print(type(x))
```

- Numbers
- String
- Sequence types: `list, tuple, range`
- mapping type: `dict`
- Set types: `set`
- Boolean type: `bool`

![quick view](./data_type.png) 

### Numbers

int, float, complex

```python
// int
x = 20

// float
x = 20.1

// complex
x = 1j
```

What will be different to Java?
```python
x = 1 / 2 

// result
0.5
```

### String

```python
x = "John"
x = 'John'
x = " John's Boy "
```

What different to Java?
```python
// this is string, not char
x = 'John'
```

### Lists - surround with `[]`

```python
[1, 2, 3]

['hi', 1, 2]

my_list = ['yo', 1, [2, 3]]

my_list[0] // 'yo'

my_list[1:]     // [1, [2, 3]]

my_list[:1]     // 'yo'

my_list[0] = 'jojo'     // replace it by new str

my_list[2][1]   // 2
```

#### enumerate the List (get the index)

```python
animals = ['Dog', 'Cat', 'Wolf']

for idx, e in enumerate(animals):
    print('#{}: {}'.format(idx + 1, e))

// output
#1: Dog
#2: Cat
#3: Wolf
```

#### List comprehension

```python
nums = [0, 1, 2, 3, 4]

// function way
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

// make with comprehension
squares = [x ** 2 for x in nums]


// moreover, with condition
squares = [x ** 2 for x in nums if x % 2 == 0]
```

### Dictionary - Java map , surround with `{}`

**The key and value is not constrained to a type.** 

```python
d = {'key1': 'item1', 'key2': 'item2'}

x = d['key1'] // get 'item1'
```

#### check if key exist

```python
d = {'cat': 'cute', 'dog': 'furry'}

print('cat' in d) // get True
```

#### or else get
If the key not exist, give default value

```python
d.get('key', 'default_value')
```

#### delete the key

```python
del d['cat']
```

#### iterate key value in dictionary

```python
d = {'cat': 'cute', 'dog': 'furry'}

for k, v in d.items():
    print('{} : {}'.format(k, v))
```

#### dictionary comprehensive

it's similar to list comprehensive. 

```python
myList = [1, 3, 5, 7, 9]

myMap = {x : x * -1 for x in myList}

for k, v in myMap.items():
    print('{} : {}'.format(k, v))
```

Output:
```
1 : -1
3 : -3
5 : -5
7 : -7
9 : -9
```

### Tuple - immutable object compared to other types - surround with `()`

> One of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot.

```python
t = (1, 2, 3)

x = t[0]    // get 1
```

### Set - surround with `{}`

```python
a = {1, 2, 2, 3, 3}

// this will get to
{1, 2, 3}
```

## Comparison Operators

```python
1 > 2
1 < 2

1 >= 1
1 <= 2

1 == 1

'hi' == 'bye'
```

### Logic operators

```python
(1 > 2) and (2 < 3)

(1 > 2) or (2 < 3)
```

## Condition - if statement

```python
if 1 < 2:
    print('Yep')

--- 

if 1 < 2:
    print('first')
else:
    print('last')

---

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')
```

## loops

### for loops


The following example, the `x` is the variable:
```python
seq = [1, 2, 3, 4, 5]

for x in seq:
    print(x)
```

### while

```python
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1
```

Output
```
i is: 1
i is: 2
i is: 3
i is: 4
```

### Range- like Java `IntStream#range`

```python
for i in range(5):
    print(i)
```

Output
```python
0
1
2
3
4
```

You can fill the list as well:
```python
list(range(5))

// get [0, 1, 2, 3, 4]
```

## Function

```python
# function w/o param                                                                      
def hello():    
    print('Hello!')    
    
# function w/ @param    
def hello(name):    
    print('Hello, ' + name)    
    
# func return value    
def getForturn(r):    
    if r == 1:    
        return "You're lucky"    
    elif r == 2:    
        return "Extra lucky!"    
fortune = getForturn(2)
```

We can define the function to take optional keyword arg:
```python
def hello(name, loud=False):
    if loud:
        print('HELLO, {}'.format(name.upper()))
    else:
        print('Hello, {}!'.format(name))

hello('Bob')
hello('Fred', loud=True)
```

What different to Java
> Java doesn't have pure function, you must use a Object provided by a class or an Object's method

## Lambda

Note that the far left is the function name, and it's assigned with `lambda ...`
```python
x = lambda a : a + 10
print(x(5))     // output 15
```

## map and filter - like Java `Stream` methods

### map
Think of it as the Java `Stream#map`

Example:
```python
seq = [1,2,3,4,5]
times2 = lambda x: x * 2

out = map(times2, seq)  // we map it to every item

x = list(out)           // now we convert to list

print(x)                // [2, 4, 6, 8, 10]
```

Use it with lambda to replace the above:
```python
list(map(lambda var: var*2,   seq))
```

### filter

Think of `Stream#filter()`

```python
seq = [1,2,3,4,5]
x = filter(lambda item: item%2 == 0, seq)

// output
y = list(x)   //  [2, 4]
```

## methods

### method of data type

```python
str = "HELLO"

toLower = str.lower()
```

### method of collection

#### get dictionary key and value

```python
d = {'key1': 'item1', 'key2': 'item2'}

// keys
d.keys()

// values
d.items()
```

#### list 

Queue
```python
list = [1, 2, 3]

list.pop()  // 3, only left [1, 2]
```

`#contain`
```python
x in [1, 2, 3]  // False

'x' in ['x','y','z']    // True
```

# import packages/library

```python
import numpy as aliasName
```
