# Use pandas

Note that the package name is **pandas**. `Panda`, on the other hand, is a cloud-service. It's to do with video and audio.

```python
import pandas as pd
```

## Read csv file

```python
import pandas as pd
df = pd.read_csv(r'~/Path/To/file.csv')
print(df)
```

## Manipulate the data

### `head(num)`

> much like Linux `head` command

Read the first `num` of rows

```python
df.head(10)
```

### `tail(num)`

> much like Linux `tail` command

```python
df.tail(4)
```

## Shape

```python
df.shape
```

## size

it's the rows multiply columns
```python
df.size
```

## length

Gives the number of rows

```python
len()
```

## columns

The columns value

```python
df.columns
```

## Access like dictionary

Get the column named *Year* 

```python
# all
df['Year']

# after 5
df['Year'][:5]
```

### Access more columns by passing array

Notice that it requires array
```python
# all
df[['Year', 'Hired']]

# sublist
df[['Year', 'Hired']][:5]
```

### Sort it

```python
df.sort_values(['Years'])
```

### count

Choose one column and count it

```python
degree_counts = df['Level of Education'].value_counts()
```

Output might look like:
```
BS     7
PhD    4
MS     2
Name: Level of Education, dtype: int64
```

## Output its to diagram

Make plots of Series or DataFrame. By default, matplotlib is used

```python
degree_counts.plot(kind='bar')
```

### methods

#### remove none, NaN value 

```python
df = df['sth'].dropna()
```

#### map value to boolean based on condition

[doc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html) 

```python
>>> df = pd.DataFrame({'cost': [250, 150, 100],
...                    'revenue': [100, 250, 300]},
...                   index=['A', 'B', 'C'])
>>> df.eq(100)
    cost  revenue
A  False     True
B  False    False
C   True    False
```
