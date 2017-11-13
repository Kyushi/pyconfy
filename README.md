# YConPy - Yaml config to Python 

## Requirements

Python 3.6

### About

Pronunciation: _[why-con-pie]_ 

When working with a yaml config file, I was annoyed that I could not use auto completion in my favourite Pyton IDE, so I decided to read the config into a Python file with a class for each set of keys. Since having to add the keys in both the yaml file and in the python file is tiresome and error-prone, I came up with YConPy. 
This reads all keys and values from the yaml file and writes a python file with classes that reflect the yaml faithfully.

*Example:*
```
Data:
  data_dir: 'data'
  
  Files:
    filename: 'file.csv'
```

returns:

```python
class Data:
    data_dir = 'data'
    class Files:
        filename = 'file.csv'
```

so that you can use this as
```
Data.Files.filename
```
in your code.

The script does this by reading the yaml file using the standard yaml module, generating a string from it and writing that to a `.py` file.

## Usage

The following command line arguments are required:

 Arg | Help | Notes
 --- | --- | ---
 yaml | Path to yaml file | Planned feature: Yaml dir will be used as output file dir
 root | Path to root directory of your project | -
 out_file 

