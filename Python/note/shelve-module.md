We can save variable by the shelve module. It helps us to save, reload the variable. It'll create files in the directory

No need to use `write()`
1. open the file
2. close the file

It works like `Dictionary`, **close() it after use.** 

Create a shelve file
```python
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
```

Read
```python
shelfFile = shelve.open('mydata')
type(shelfFile)
#   <class 'shelve.DbfilenameShelf'>

shelfFile['cats']
#   ['Zophie', 'Pooka', 'Simon']

>>> shelfFile.close()
```

Dictionary-like methods
- keys()
- values()

**Note: the return values aren't really a list, use `list()` to cast.** 
```python
shelfFile = shelve.open('mydata')
list(shelfFile.keys())
#   ['cats']
list(shelfFile.values())
#   [['Zophie', 'Pooka', 'Simon']]
shelfFile.close()
```
