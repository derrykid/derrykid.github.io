- inputStr()
- inputNum()
- inputChoice()
- inputMenu()
- inputDatetime()
- inputYesNo() - custome yes or no: `pyip.inputYesNo(prompt, yesVal='sí', noVal='no') `
- inputBool()
- inputEmail()
- inputFilepath()
- inputPassword()
- inputCustom(functionName) - a custom function

#### prompt, blank, limit, timeout, default, allowRegexes, blockRegexes
prompt text
```python
response = pyinputplus.inputInt(prompt='Enter a number: ')
Enter a number: cat
'cat' is not an integer.
Enter a number: 42
```

Accept blank input
```python
response = pyip.inputNum(blank=True)
```

Retry limit: if not valid input for few times, it terminates
```python
response = pyip.inputNum(limit=2)
```

Timeout, second:
```python
response = pyip.inputNum(timeout=10) # 10 seconds
```

Default value:
```python
response = pyip.inputNum(limit=2, default='134') # give a default value 134 when fails
```

Regex example: this program only accepts odd number
```python
response = pyip.inputNum(blockRegexes=[r'[02468]$'])
42
This response is invalid.
44
This response is invalid.
43
```

#### inputNum()
- min
- max
- greaterThan
- lessThan

Example
```python
response = pyip.inputNum('Enter number: ', min=4, lessThan=6)
```

#### Custom function
Pass the function name without `()`
```python
# custom function
>>> def addsUpToTen(numbers):
...   numbersList = list(numbers)
...   for i, digit in enumerate(numbersList):
...     numbersList[i] = int(digit)
...   if sum(numbersList) != 10:
...     raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
...   return int(numbers) # Return an int form of numbers.
...

response = pyinputplus.inputCustom(addsUpToTen)
```
