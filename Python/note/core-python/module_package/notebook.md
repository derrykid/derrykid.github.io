```python
from IPython.core.display import HTML

HTML(
    """
<style>
    .jp-Cell-inputWrapper:has(.jp-MarkdownOutput) .jp-RenderedMarkdown {
        border-style: dashed hidden hidden hidden;
        border-color: red;
    }
</style>
"""
)
```





<style>
    .jp-Cell-inputWrapper:has(.jp-MarkdownOutput) .jp-RenderedMarkdown {
        border-style: dashed hidden hidden hidden;
        border-color: red;
    }
</style>




# module, package, and class

- module: it's any `.py` script. Any single is considered as a module
- package: a collection of module(s) along with `__init__.py`

Tree view of current directory:
```
.
├── module_package.ipynb
├── package_and_modules
│   ├── carspackage
│   │   ├── cars.py
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   └── suv.py
│   │     
│   └── cars.py
│
└── rabbit.py
```

## module
Under current directory, there is a `rabbit.py` script. 
Inside, there's a class `Rabbit`. It's consider a module:


```python
import rabbit

type(rabbit)
```




    module



We are sometimes more interested in how to create an object from the class, in that regard:

`obj = module.Class(args)`


```python
hare = rabbit.Rabbit(color="white")
hare
```




    A rabbit of color: white



## A module inside a directory (not a package!)
under the directory `package_and_modules`, there is a py script:
- `cars.py`, a single class `Car` inside

```
.
├── module_package.ipynb
├── package_and_modules
│   ├── carspackage
│   │   ├── cars.py
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   └── suv.py
│   │     
│   └── cars.py
│
└── rabbit.py
```

We can make use of `from` keyword:
```
from package import module
```


```python
from package_and_modules import cars

car = cars.Car(make="Lexus", model="Lx")
car
```




    Make Lexus, model: Lx



### from module import the class

To remove the preceding `module.Class()`:
```python
from package.module import Class
```


```python
from package_and_modules.cars import Car

supercar = Car("Lambo", model="supercar")
supercar
```




    Make Lambo, model: supercar



## package

> package: a collection of module(s) along with `__init__.py`

We have a directory `carspackage/` along with `__init__.py`. This is considered a python package:

```
carspackage/
|
├── cars.py
├── __init__.py
├── __main__.py
└── suv.py
```


```python
%cd package_and_modules/
```

    /home/derry/Python/note/core-python/module_package/package_and_modules



```python
from carspackage import suv

car = suv.SUV("suv", "ranger")
```

    I am outside the guard!
    SUV Init success!!


### Run the package, `__main__.py` is the starting point

Instead of running `python myscript.py`, you can also run the package
`python {package_name}`

`__main__.py` will be the starting point


```python
!python carspackage
```

    __name__:  cars
    I am outside the guard!
    Make is Toyota, Model is RAV4
    
    ---------------------------
    
    
    SUV Init success!!
    Make is Lexus, Model is Renger
    
    ---------------------------
    
    


## Difference of `__init__.py` and ` __main__.py`

- `__init__.py` is run when **you import the module.**
- `__main__.py` is run when **you directly run the module.**

Again, Python recognize the directory with `__init__.py` as a module.

Tree view
```
./app
├── cryingout.py
├── __init__.py
└── __main__.py
```

From parent directory:
```bash
python app  # this will run __main__.py
```

In Python shell:
```python
>>> import app  # this will run __init__.py
>>>
```

## `__init__.py` use case

`__init__.py` is run when you import the python module. For example:
```python
>>> import pandas as pd
```

When import `pandas` package, the `pandas.__init__.py` will run. As the name suggests, it initializes. So inside that, you can initialize any global variables, etc.


