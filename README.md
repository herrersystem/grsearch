# Gramsearch
Search keyword within string chars and files. More complete than _str.find(keyword)_ function.

## Installation
```
$ pip install grsearch
```
### Compatibility
- Python3.4
- Linux/Windows

## Usage

```
import grsearch

text="""
  Python interpreters are available for installation on many operating systems,
  allowing python code execution on a wide variety of systems.
  """
keywords=['python','systems']

#return list [[keyword, number_of_occurences, [positions]]
result=search(test, keywords)

print(result)
```

```
[['python', 2, [0, 87]], ['systems', 2, [69, 130]]]
```
### Examples with more parameters :
```
result=search(test, keywords, case_sensitive=True)
print(result)
```

```
[['python', 1, [87]], ['systems', 2, [69, 130]]]
```

```
result=search(test, keywords, limit_iteration=1)
print(result)
```

```
[['python', 1, [87]], ['systems', 2, [69, 130]]]
```
