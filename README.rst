==============================
YConPy - Yaml config to Python
==============================

Requirements
------------

Python 3.6

About
-----

Pronunciation: *[why-con-pie]*

When working with a yaml config file, I was annoyed that I could not use auto completion in my favourite Pyton IDE, so I decided to read the config into a Python file with a class for each set of keys. Since having to add the keys in both the yaml file and in the python file is tiresome and error-prone, I came up with YConPy.
This reads all keys and values from the yaml file and writes a python file with classes that reflect the yaml faithfully.

*Example:*

A file `myconfig.yaml`
::

    Data:
      data_dir: 'data'

      Files:
        filename: 'file.csv'

returns `myconfig.py`:

.. code-block:: python

    class Data:
        data_dir = 'data'
        class Files:
            filename = 'file.csv'

so that you can use this as

.. code-block:: python

    import myconfig
    myconfig.Data.Files.filename

in your code.

The script does this by reading the yaml file using the standard yaml module, generating a string from it and writing that to a ``.py`` file.

Usage
-----

Download
~~~~~~~~

.. code-block::

    git clone https:github.com/Kyushi/yconpy.git


Install
~~~~~~~

.. code-block::

    pip install .


Run
~~~

.. code-block::

    python -m yconpy [yaml] [root]


Use the following command line arguments (if applicable):

+-----+----------------------------------------+-------------------------------------------------------------------+
| Arg | Help                                   | Notes                                                             |
+=====+========================================+===================================================================+
|yaml | Path to yaml file                      | Yaml dir and filename will be used as output file name and dir    |
+-----+----------------------------------------+-------------------------------------------------------------------+
|root | Path to root directory of your project | (For future use of adding absolute paths)(optional)               |
+-----+----------------------------------------+-------------------------------------------------------------------+
|name | Name of Base class                     | Base class, of which all config elements are a subclass (optional)|
+-----+----------------------------------------+-------------------------------------------------------------------+
