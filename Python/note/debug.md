#### Assertion
Assertion can fast fail your program
```python
a = 1
b = 2
assert a + b == 10
```

Alternatively, print the value
```python
aList = ['yellow', 'green']
assert 'red' in aList, 'Neither light is red! ' + str(stoplight)
```

#### exception
We can `raise Exception` by try, exception block
```python
def box(a, b):
    if a is not b:
        raise Exception('These are not equal!')

try:
    box(a, b)
except Exception as err:
    print('An exception happened: ' + str(err))
```

#### Using logging
```python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5))
logging.debug('End of program')
```

Logging Levels

| Level    | Logging function   | Level |
|----------|--------------------|-------|
| DEBUG    | looging.debug()    | 1     |
| INFO     | logging.info()     | 2     |
| WARNING  | logging.warning()  | 3     |
| ERROR    | logging.error()    | 4     |
| CRITICAL | logging.critical() | 5     |

As we can pass the level to the `logging.basicConfig()` to specify the errors we want to see. For example, this will show only `ERROR` level and the level above `CRITICAL`:
```python
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s -  %(message)s')
```

Disable logging, it will disable the target level and lower. This code disable all levels:
```python
logging.disable(logging.CRITICAL)
```

Logging to a file, specify the file name
```python
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s -  %(levelname)s -  %(message)s')
```
