> Used for copy files, directories

`import shutil`

#### Copy

Copy a file to a folder
```python
import shutil, os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')
```

`shutil.copytree()`: Copy entire folder
```python
import shutil, os
from pathlib import Path
p = Path.home()
shutil.copytree(p / 'spam', p / 'spam_backup')
```

#### move
**Consider this as shell command `mv source dest`** 

`shutil.move(source, dest)`: return a string of path
```python
shutil.move('C:\\bacon.txt', 'C:\\eggs')
```

#### delete files and folders

- os.unlink(path) - delete the file at the path
- os.rmdir(path) - remove the empty dir
- shutil.rmtree(path) - remove recursively

```python
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)
```

#### send files to bin

`import send2trash` download the package
```python
send2trash.send2trash('bacon.txt')
```

#### Print directory tree - `os.walk(path)`

```python
for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
```

#### zip file

Read, **close() after read** 
```python
import zipfile, os
from path import Path

p = Path.home()
exampleZip = zipfile.ZipFile(p/'example.zip')   # path of file
files = exampleZip.nameList()                   # give use the file list in zip
zipInfo = exampleZip.getinfo('file.txt')
print(zipInfo.file_size)
print(zipInfo.compress_size)

exampleZip.close()
```

Extract all
```python
import zipfile, os
from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p/'example.zip')
exampleZip.extractAll()     # default, pwd. Optionally, pass the path
exampleZip.close()
```

Extract a single file
```python
exampleZip.extract('spam.txt')  # 2nd param optional for destination
```

Create/add to zip file: if append the file, use `a` to ZipFile(), like write
```python
import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) # this algorithm works well on all types of data
newZip.close()
```
