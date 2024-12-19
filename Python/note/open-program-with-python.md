Launch programs from python. **It's different process and threads.** 

```python
import subprocess
subprocess.Popen('/usr/bin/midori')     # P stands for process
```

## `poll()`, `wait()` methods
- `web.poll()` - it returns None until the process terminates. Return an integer exit code
- `web.wait()` - It won't return anything until the process terminates. Return integer exit code
```python
web = subprocess.Popen('/usr/bin/midori')
>>> web.poll() == None
True
>>> web.wait()      # show nothing until we close the web process
>>> web.poll
# return 0
```

## Passing cmd args to the Popen()
Pass a list of String to `Popen()`. Not every GUI use command line args as extensively as command line programs do. But some accept one args.
```python
subprocess.Popen(['A', 'B'])

# open with text editor
subprocess.Popen(['/usr/bin/mousepad', '/home/derry/Java/note/lombok.md'])
```

Run python scripts in python
```python
subprocess.Popen(['/usr/bin/python', '/home/derry/Python/hello.py'])
```

## Open with default Applications
It'd open with default application like NotePad, etc
- Win: start
- Mac: open
- Linux: xdg-open

```python
subprocess.Popen(['xdg-open', 'project-idea.md'])
```
