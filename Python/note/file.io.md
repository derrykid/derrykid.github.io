Import package, specify `Path`, otherwise we have to type `pathlib.Path` every time
This library will ensure it works on all OS.

> preferably, programmers save variables as `shelve module` instead of `.py`

#### Path

Use `Path` to create Operation system based file path
```python
Path('spam', 'bacon', 'eggs')
# WindowsPath('spam/bacon/eggs')

str(Path('spam', 'bacon', 'eggs'))
# 'spam\\bacon\\eggs'
```

**/ operator to join paths**: it can work to concatenate path
```python
Path('spam') / 'bacon' / 'eggs'
# WindowsPath('spam/bacon/eggs')
Path('spam') / Path('bacon/eggs')
# WindowsPath('spam/bacon/eggs')
Path('spam') / Path('bacon', 'eggs')
# WindowsPath('spam/bacon/eggs')
```

pwd
```python
Path.cwd()
```

mkdir: one directory at a time
```python
Path('path').mkdir()
```

Attributes of path: all are string but `p.parent`
- p.anchor
- p.parent - Path object
- p.name
- p.stem
- p.suffix
- p.drive

```python
>>> p = Path('C:/Users/Al/spam.txt')
>>> p.anchor
'C:\\'
>>> p.parent # This is a Path object, not a string.
WindowsPath('C:/Users/Al')
>>> p.name
'spam.txt'
>>> p.stem
'spam'
>>> p.suffix
'.txt'
>>> p.drive
'C:'
```


#### os
`import os`

- os.chdir(path)
- os.makedirs(path)
- os.path.abspath(path)
- os.path.isabs(path): boolean
- os.path.relpath(path, start) - relative path
- os.path.dirname(path)
- os.path.basename(path)
- os.path.split(path) - get a tuple of  `dirname` & `basename` 
- os.path.join(path, fileName) - concatenate the path
- os.sep - var of the directory-separator e.g. '/' in Linux

Change directory
```python
os.chdir('path')
```

Create a new dir: can make recursively if not exist
```python
os.makedirs('path')
```

#### file size and folder contents
- os.path.getsize(path): get the size in bytes of the file
- os.listdir(path): `ls -a`. See `glob()` for list directory use

Total size of directory:
```python
totalSize = 0
for fileName in os.listdir('/home/derry/Documents'):
    totalSize = totalSize + os.path.getsize(os.path.join('/home/derry/Documents', fileName))
print(totalSize)
```

#### glob() - accepts regex for file matching
Path has a `glob(regex)` method to generator a list of path object
```python
p = Path('/home/derry/Java/note/')
p.glob('*.md')      # every markdown files
<generator object Path.glob at 0x7fa66bf39e00>
#   assign to a variable
list = list(p.glob('*.md'))
```

#### Validate the path

Return boolean value
- p.exist()
- p.is_file()
- p.id_dir()


#### file io

**Always close() the file** 

Open
```python
>>> helloFile = open(Path.home() / 'hello.txt', 'r')    # the second param is optional for 'read'
```

Read
```python
content = helloFile.read()          # a single string ()
content = targetFile.readlines()    # return a list of string separate by \n
```

Overwrite: second param 'w'
```python
baconFile = open('bacon.txt', 'w')   # overwrite the existing file
baconFile.write('Hello, world!\n')
baconFile.close()
```

Append: second param `'a'`
```python
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
```

#### Save as `.py`
When save as `.py` you can import the package
```python
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
```

import the package
```python
import myCats
>>> myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
>>> myCats.cats[0]['name']
'Zophie'
```
