# Regex

simple search like the following, will return a match object
```python
pattern = 'hi'
text = 'hi, this is derry'
return_object_match = re.search(pattern, text)
```

If not found, the `match` object is `NoneType`

## match object

After the search, the return is an object `Match`
```python
text = 'Hello, ATU'

#1 import library
import re

#2 create pattern
pattern = 'ATU'

#3 search
match = re.search(pattern, text)
```

### Access the result - `match.group()`

When finds the match, we can use `group()` to access the `match` object 

```python
text = '032-12-35231'
pattern = r'(\d{3})-(\d{2})-(\d{5})'

match = re.search(pattern, text)

match.group()  # '032-12-35231'
match.group(0) # '032-12-35231'
match.group(1) # '032'
match.group(2) # '12'
match.group(3) # '35231'
```

### match position

Get the span, it shows where is the matched text
```python
# a tuple of ints
match.span()  # (7, 10)

match.start() # 7
match.end()   # 10
```

### Use `finditer()` for every match - iterator object

Use `search()` will only return the first occurrence. Use `finditer()`. It will return an iterator
```python
text = "I am a student in ATU and I think ATU is great."
pattern = 'ATU'

matches = re.finditer(pattern, text) # an iterator of all matches

# a match: <re.Match object; span=...>
for match in matches:
    # do sth with the match object
```


## Create pattern

### Special sequence

- Create pattern by `r'pattern'`. `r''` is raw string, will not intepret `\n, \t, etc`

| Char | Desc              | Code ex | Match |
|------|-------------------|---------|-------|
| \d   | digit             | a-\d-b  | a-1-b |
| \w   | alphanumberic     | \w-\w\w | g-3c  |
| \s   | white space       | a\sb\sc | a b c |
|------|-------------------|---------|-------|
| \D   | non digit         | \D\D    | Ac    |
| \W   | non-alphanumberic | \W\W    | *+    |
| \S   | non-white space   | \S\S    | Y3    |

If we want to find numbers, e.g. `320-1823`. The regex will be: `r'\d\d\d-\d\d\d\d'`. There are repetitive. We can use *quantifiers* to reduce the duplications.

### Quantifiers

Quantifiers basically tell regex **how many times it appears.** 

For example, The number:
```python
# pattern for 312-3425
pattern = r'\d\d\d-\d\d\d\d'

# use quantifiers
pattern = r'\d{3}-\d{4}'
```

| Char   | Desc               | Code ex        | Match           |
|--------|--------------------|----------------|-----------------|
| +      | 1 or more          | version \w-\w+ | version a-31    |
| {2}    | Exactly 2 times    | \D{2}          | hey             |
| {2, 4} | 2 ~ 4 times        | \d{2, 4}       | 312             |
| {3,}   | occurs 3+ times    | \w{3,}         | abc, abce, aeed |
| \*     | zero or more times | A\*B           | AB, AAB,AAAAAB  |
| ?      | 0 or once          | plurals?       | plural, plurals |

### `()` brackets for set or chars to match

We can use `()` to create a group: `r'(\d{3})-(\d{3})'`. This matches something like `123-321`, `231-324`. The brackets will not be included.

Example:
```python
pattern = r'(\d{3})-(\d{2})-(\d{5})'

match = re.search(pattern, text)

match.group()  # '032-12-35231'
match.group(0) # '032-12-35231'
match.group(1) # '032'
match.group(2) # '12'
match.group(3) # '35231'
```

### `[]` square brackets for a set of characters to match

Inside the square brackets, it's a set. You can specify what you want, or what you do not want.

For example `r'Pi[aptg]'` gives us the combination of :
- Pia
- Pip
- Pit
- Pig

```python
pattern = r'Pi[aptg]'
reg_1 = re.search(pattern, 'Pip')
reg_2 = re.search(pattern, 'Pig')

print(reg_1) # <re.Match object; span=(0, 3), match='Pyp'>
print(reg_2) # <re.Match object; span=(0, 3), match='Rig'>
```

#### The `^` inside `[]` square brackets

The `^` means **not** in square brackets.

```python
# this means not digit
pattern = r"[^\d]"

text = 'Haha, so 32 code a lot and 27 is her fav'
re.findall(pattern, text)

# output
['H', 'a', 'h', 'a', ',', ' ', 's', 'o', ' ', ' ', 'c', 'o', 'd', 'e', ' ', 'a', ' ', 'l', 'o', 't', ' ', 'a', 'n', 'd', ' ', ' ', 'i', 's', ' ', 'h', 'e', 'r', ' ', 'f', 'a', 'v']
```

### Special characters e.g. `|, ., ?` etc

#### `|` is `or`
```python
# finds man or woman
pattern = r'man|woman'
```

#### `.` - for *anything*
```python
text ="The cat sat on the mat and then went splat"
re.findall(r"..at", text)
```
Output: note, there is a white space before the ' cat'
```python
' cat', ' sat', ' mat', 'plat'
```

#### Start with `^`, end with `$`, match before linebreak

*Note, `^` in square brackets `[]` is different to this.* 

Use `^` for begining
```python
pattern = r"^\d"
text = "1 divided by 0 gives an error."
re.findall(pattern, text) # ['1']
```

Use `$` for ending
```python
pattern = r'\d$'

re.findall(r"\d$", "Second floor of ATU Donegal end with a 2") # ['2']

# this one not found, cuz it ends with a dot '.'
re.findall(r"\d$", "Second floor of ATU Donegal end with a 2.") # []
```

#### `\A`, `\z`, `\b`

##### Consider `\A` is like `^` but it's for whole string

```python
>>> text = 'Haha, so 32 code a lot and da27 is her fav'
>>> pattern = r'\A'
>>> re.findall(pattern, text)
['']
>>> pattern = r'\A[Ha]'
>>> re.findall(pattern, text)
['H']
>>> pattern = r'\A[Ha]+'
>>> re.findall(pattern, text)
['Ha']
>>> pattern = r'\A\w+'
>>> re.findall(pattern, text)
['Haha']
```

##### `\b` only matches the word

Imagine this `\b` **represents a boundary.** 

```python
text = 'Hello, I am derry, and this is my number 321-312 and thanks'

# It will match
# '312-312'
# '.312-123.'
# ' 312-324 '
# '!312-324!'
pattern = r'\b(\d{3})-(\d{3})\b'

re.search(pattern, text) # '321-312'
```

## Example: match the domain name

Only match `atu`
```python
urls = ['http://atu.ie', 'https://www.atu.ie', 'http://www.atu.ie/donegal/']

pattern = r'(http(s)?:\/\/(www\.)?)' + '([\w]*)' + '(\.)?(\W){1}(\w)+'

for url in urls:
  matches = re.search(pattern, url)
  print(matches.group(4))
```

In the regex: I create many `()` sets. It matches different pair.
