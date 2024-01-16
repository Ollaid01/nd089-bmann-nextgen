"""
The Python Standard Library has a lot of modules! To help you get familiar with what's available, here are a selection of our favourite Python Standard Library modules and why we use them!

    csv: very convenient for reading and writing csv files
    collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
    random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
    string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
    re: pattern-matching in strings via regular expressions
    math: some standard mathematical functions
    os: interacting with operating systems
    os.path: submodule of os for manipulating path names
    sys: work directly with the Python interpreter
    json: good for reading and writing json files (good for web work)

We hope you find these useful!
"""


"""
Techniques for Importing Modules

There are other variants of import statements that are useful in different situations.

    To import an individual function or class from a module:

from module_name import object_name

    To import multiple individual objects from a module:

from module_name import first_object, second_object

    To rename a module:

import module_name as new_name

    To import an object from a module and rename it:

from module_name import object_name as new_name

    To import every object individually from a module (DO NOT DO THIS):

from module_name import *
    ```
    6. If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.
    ```python
import module_name
"""


"""
Modules, Packages, and Names

In order to manage the code better, modules in the Python Standard Library are split down into sub-modules that are contained within a package. A package is simply a module that contains sub-modules. A sub-module is specified with the usual dot notation.

Modules that are submodules are specified by the package name and then the submodule name separated by a dot. You can import the submodule like this.

import package_name.submodule_name
"""


"""
Third-Party Libraries

There are tens of thousands of third-party libraries written by independent developers! You can install them using pip, a package manager that is included with Python 3. pip is the standard package manager for Python, but it isn't the only one. One popular alternative is Anaconda which is designed specifically for data science.

To install a package using pip, just enter "pip install" followed by the name of the package in your command line like this: pip install package_name. This downloads and installs the package so that it's available to import in your programs. Once installed, you can import third-party packages using the same syntax used to import from the standard library.
Using a requirements.txt File

Larger Python programs might depend on dozens of third party packages. To make it easier to share these programs, programmers often list a project's dependencies in a file called requirements.txt. This is an example of a requirements.txt file.

beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1

Each line of the file includes the name of a package and its version number. The version number is optional, but it usually should be included. Libraries can change subtly, or dramatically, between versions, so it's important to use the same library versions that the program's author used when they wrote the program.

You can use pip to install all of a project's dependencies at once by typing pip install -r requirements.txt in your command line.
Useful Third-Party Packages

Being able to install and import third party libraries is useful, but to be an effective programmer you also need to know what libraries are available for you to use. People typically learn about useful new libraries from online recommendations or from colleagues. If you're a new Python programmer you may not have many colleagues, so to get you started here's a list of packages that are popular with engineers at Udacity.

    IPython - A better interactive Python interpreter
    requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
    Flask - a lightweight framework for making web applications and APIs.
    Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
    Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
    pytest - extends Python's builtin assertions and unittest module.
    PyYAML - For reading and writing YAML files.
    NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
    pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
    Matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
    ggplot - Another 2D plotting library, based on R's ggplot2 library.
    Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
    pyglet - A cross-platform application framework intended for game development.
    Pygame - A set of Python modules designed for writing games.
    pytz - World Timezone Definitions for Python
"""