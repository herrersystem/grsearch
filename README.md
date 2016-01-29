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

### With string characters
```
import grsearch

text="""
  Python interpreters are available for installation on many operating systems,
  allowing python code execution on a wide variety of systems.
  """
keywords=['python','systems']

#return list [[keyword, number_of_occurences, [positions]]
result=grsearch.search(text, keywords)

print(result)
```

```
result: [['python', 2, [0, 87]], ['systems', 2, [69, 130]]]
```
### Examples with more parameters :
```
result=grsearch.search(text, keywords, case_sensitive=True)
print(result)
```

```
result: [['python', 1, [87]], ['systems', 2, [69, 130]]]
```

```
result=grsearch.search(text, keywords, limit_iteration=1)
print(result)
```

```
result: [['python', 1, [0]], ['systems', 1, [69]]]
```

### With files
```
import grsearch

path_file="Documents/text.txt"
keywords=['python','systems']

#return list [[keyword, number_of_occurences, [positions]]
result=grsearch.search_infile(path_file, keywords)

print(result)
```

```
result: [['python', 2, [0, 87]], ['systems', 2, [69, 130]]]
```
All parameters (case_sensitive, limit_iteration, exactly) is available with search within file.

### Parameter __exactly__

```
import grsearch

text="I'm herrersystem and my operating system is not windows."
keywords=['system']

#return list [[keyword, number_of_occurences, [positions]]
result=grsearch.search(text, keywords, exactly=True)

print(result)
```

```
result: [['system', 1, [34]]]
```

_Result with exactly = False_

```
result: [['system', 2, [10, 34]]]
```
