## Multithreading

**Note: Passing the methods, not call the method** 
```python
import threading, time

def takeANap():
    time.sleep(5)
    print('wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program')
```

## Passing args to the thread's func
```python
threadObj = threading.Thread(target=print, args['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()

# Output: Cats & Dogs & Frogs
```

## Concurrency Issues
> To avoid concurrency issues, never let multiple threads read or write the same variables. When you create a new Thread object, make sure its target function uses only local variables in that function. This will avoid hard-to-debug concurrency issues in your programs.


## Multithread example: Download comics

We use the download comics images example. The function `downloadXkcd` is the function that make requests, create soup, and save to the file.
```python
import requests, os, bs4, threading
def downloadXkcd(startComic, endComic):
    # requests, soup, save scripts
    
downloadThreads = [] # a list of all threads
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    
    # add thread to list
    downloadThreads.append(downloadThread)
    # start the thread
    downloadThread.start()
```
We created 14 threads in the pool and added to the `downloadThreads` list. In the end, we started the threads.

<br>

**Wait for all threads to end**

The main thread moves on even when we created multiple threads. There are times that we might want our main thread to wait until all other threads are finished. We can use `join()` to wait until all done.
```python
for each in downloadThreads:
    each.join()
print('Done')
```
Here, the main thread won't proceed until all other threads are finished.

