""""
Making a Package

In the previous section, the Distribution and Gaussian code was refactored into individual modules. A Python module is just a Python file containing code.

In this next section, you'll convert the Distributions code into a Python package. A package is a collection of Python modules.

Although the previous code might already seem like it was a Python package because it contained multiple files, a Python package also needs an __init__.py file. In this section, you'll learn how to create this __init__.py file and then pip install the package into your local Python installation.



===

You can complete this entire lesson within the classroom using the provided workspaces; however, if you want to develop a package locally on your computer, you should consider setting up a virtual environment. That way if you install your package on your computer, the package won't install into your main Python installation. Before starting the next exercise, the next part of the lesson will discuss what virtual environments are and how to use them.
Follow along with the video

Just to test using the pip command, you can try this

pip install scikit-learn
Preparing a package

To get your package ready so the can be pip installed by others, lets do a couple things

In a folder, you will need 2 things

    distributions folder
    setup.py file

In the example from the previous page. this distributions folder currently contains the

    Gaussiandistribution.py
    Generaldistribution.py
    __init__.py
        inside this file, we include any imports so we have from .Gaussiandistribution import Gaussian

In the setup.py file, which is the first file that pip looks for when installing. you see this code

from setuptools import setup

setup(name="distributions", 
 version="0.1",
 description="Gaussian distributions", 
 packages=['distributions'],
 zip_safe=False)

Now we are ready to create the package. Make you are in the directory with the distribution folder and setup.py file. Then type

pip install .

This installs our package. It means that we can use the code as if it were part of Python.
Testing your newly installed package

Type Python then at the >>> prompt, type from distributions import Gaussian. This will bring your code into memory for access. Lets try it now

gaussian_one = Gaussian(10,5)
gaussian_one.mean
gaussian_one.stdev


Object-Oriented Programming and Python Packages

A Python package does not need to use object-oriented programming. You could simply have a Python module with a set of functions. However, most if not all of the popular Python packages take advantage of object-oriented programming for a few reasons:

    Object-oriented programs are relatively easy to expand especially because of inheritance
    Object-oriented programs obscure functionality from the user. Consider scipy packages. You don't need to know how the actual code works in order to use its classes and methods.

    ====

========

Virtual Environments
Python Environments

In the next part of the lesson, you'll be given a workspace where you can upload files into a Python package and pip install the package. If you decide to install your package on your local computer, you'll want to create a virtual environment. A virtual environment is a silo-ed Python installation apart from your main Python installation. That way you can install packages and delete the virtual environment without affecting your main Python installation

Let's talk about two different Python environment managers: conda and venv. You can create virtual environments with either one. Below you'll read about each of these environment managers including some advantages and disadvantages. If you've taken other data science, machine learning or artificial intelligence courses at Udacity, you're probably already familiar with conda.
Conda

Conda does two things: manages packages and manages environments.

As a package manager, conda makes it easy to install Python packages especially for data science. For instance, typing conda install numpy will install the numpy package.

As an environment manager, conda allows you to create silo-ed Python installations. With an environment manager, you can install packages on your computer without affecting your main Python installation.

The command line code looks something like this:

conda create --name environmentname
source activate environmentname
conda install numpy

Pip and Venv

There are other environmental managers and package managers besides Conda. For example, venv is an environment manager that comes pre-installed with Python 3. Pip is a package manager.

Pip can only manage Python packages whereas conda is a language agnostic package manager. In fact, conda was invented because pip could not handle data science packages that depended on libraries outside of Python. If you look at the history of conda, you'll find that the software engineers behind conda needed a way to manage data science packages (NumPy, Matplotlib, etc.) that relied on libraries outside of Python.

Conda manages environments AND packages. Pip only manages packages.

To use venv and pip, the commands look something like this:

python3 -m venv environmentname
source environmentname/bin/activate
pip install numpy

Which to Choose?

Whether you choose to create environments with venv or conda will depend on your use case. Conda is very helpful for data science projects, but conda can make generic Python software development a bit more confusing; that's the case for this project.

If you create a conda environment, activate the environment, and then pip install the distributions package, you'll find that the system installs your package globally rather than in your local conda environment. However, if you create the conda environment and install pip simultaneously, you'll find that pip behaves as expected installing packages into your local environment:

conda create --name environmentname pip

On the other hand, using pip with venv works as expected. Pip and venv tend to be used for generic software development projects including web development. For this lesson on creating packages, you can use conda or venv if you want to develop locally on your computer and install your package.


Instructions for venv

For instructions about how to set up virtual environments on a macOS, Linux, or Windows machine using the terminal, see Installing packages using pip and virtual environments.

Refer to the following notes for understanding the tutorial:

    If you are using Python 2.7.9 or later (including Python 3), the Python installation should already come with the Python package manager called pip. There is no need to install it.
    env is the name of the environment you want to create. You can call env anything you want.
    Python 3 comes with a virtual environment package preinstalled. Instead of typing python3 -m virtualenv env, you can type python3 -m venv env to create a virtual environment.

Once you've activated a virtual environment, you can then use terminal commands to go into the directory where your Python library is stored. And then you can run pip install ..

In the next section, you can practice pip installing and/or creating virtual environments in the classroom workspace. You'll see that creating a virtual environment actually creates a new folder containing a Python installation. Deleting this folder will remove the virtual environment.

Note that if you install packages on the workspace and run into issues, you can always reset the workspace; however, you will lose all of your work. Be sure to download any files you want to keep before resetting a workspace.

Conda does what two things? manage packages and environemetns

Does venv come preinstalled with Python? Yes it does and it can be used to manage generic software environments


===============

Binomial Class

You will only need to actually make changes to 2 files

    __init.py__ inside the distributions folder - You'll need to import the binomial package
    Binomialdistribution.py

A few note to get started

    You will need to use pip to install all required library files. In the 4_binomal_package folder,

type pip install .

    As you make changes to the files, you will need to rebuild the package as shown in the video, pip install --upgrade .
    You can use the test.py file as a unit test to make sure your code works correctly.


================================

Scikit-learn Source Code

The skills you are learning in this course will help you understand some of the code in popular packages such as Pandas, SxiPy, Numpy, and Scikit-learn. Keep in mind, there are many more advanced Python commands that you have not learned yet, but at least you have a strong foundation.

These popular packages are provided on Github, which means the source code is available to the public. As you become more familiar with programming, you can browse these packages and even contribute to them.
Contributing to a GitHub project

Here are a few links about how to contribute to a github project:

    Beginner's Guide to Contributing to a Github Project
        This is a guide to contributing to an open source project that uses GitHub.
    Contributing to a Github Project
        Public help is always welcome. Contributing is a great way to learn more about coding, while also connecting with others on Github. You can learn technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and possibly even actual contributions.

Further Learning and Resources on Advanced Python OOP Topics

Use the following resources to learn about more advanced OOP topics that appear in the scikit-learn package:

    Decorators
    Mixins

================================

PyPi vs. Test PyPi

Note that pypi.org and test.pypy.org are two different websites. You'll need to register separately at each website. If you only register at pypi.org, you will not be able to upload to the test.pypy.org repository.

Also, remember that your package name must be unique. If you use a package name that is already taken, you will get an error when trying to upload the package.
Summary of the Terminal Commands Used in the Video

cd binomial_package_files
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ dsnd-probability

# command to upload to the pypi repository
twine upload dist/*
pip install dsnd-probability

More PyPi Resources
Tutorial on distributing packages

This link has a good tutorial on distributing Python packages including more configuration options for your setup.py file: tutorial on distributing packages. You'll notice that the python command to run the setup.py is slightly different with

python3 setup.py sdist bdist_wheel

This command will still output a folder called dist. The difference is that you will get both a .tar.gz file and a .whl file. The .tar.gz file is called a source archive whereas the .whl file is a built distribution. The .whl file is a newer type of installation file for Python packages. When you pip install a package, pip will first look for a .whl file (wheel file) and if there isn't one, will then look for the tar.gz file.

A tar.gz file, ie an sdist, contains the files needed to compile and install a Python package. A .whl file, ie a built distribution, only needs to be copied to the proper place for installation. Behind the scenes, pip installing a .whl file has fewer steps than a tar.gz file.

Other than this command, the rest of the steps for uploading to PyPi are the same.
Other Resources

If you'd like to learn more about PyPi, here are a couple of resources:

    Overview of PyPi
    MIT License
    How to deploy to PyPi

========================================


Lesson review

In this lesson, we learned a lot!

First, we covered the fundamentals of object-oriented programming, including:

    Procedural vs. object-oriented programming
    Classes, objects, methods, and attributes
    Coding a class
    Magic methods Inheritance

Then we used object-oriented programming to make a Python package. In this section, we:

    Made our own package
    Took a tour of the source code inside some scikit-learn packages
    Learned how to put a package on PyPi so that it can be easily installed

Glossary of New Terms
KeyTerm	Definition
Attributes	The variables inside a class.
Class	A way to represent actual objects through programming by listing attributes to describe the characteristics of the object, as well as the methods, which define the actions that the object can perform. An object might be a car, so there is a Car class with attributes such as color, price, gas tank size, and methods such as drive or park.
docstrings	A type of comment that describes how a Python module, function, class, or method works.
Function	A function and a method are very similar. The main difference is that a method is inside of a class whereas a function is outside of a class.
Gaussian	Being or having the shape of a normal curve or a normal distribution.
Inheritance	In object-oriented programming, an object can be a child of a parent object, in which cased the child automatically "inherits" all attributes and methods of the parent class. This is used to generalize objects and is especially useful for code reuse. For example, a "Vehicle" parent class might have several child classes such as Train, Truck, and Bicycle.
Magic methods	Methods in Python that can be overridden to redefine their default action.
Methods	A named collection of code inside a class that provides action and functionality.
Modularized code	Object-oriented code that has been placed into separate files.
Object	A representation of a real-world thing by using a class.
Object-oriented programming	Also called OOP, this is where code is placed into different modularized objects. These objects represent objects in the real world.
Package	A collection of modules placed in a single directory
Procedural programming	A program written in a single file where the instructions go from top to bottom.
Scikit-learn	A library used in predictive data analysis and machine learning in Python.
self	Tells Python where to look in the computer's memory for the current object.
Virtual environment	A simulated computer that is not physical, includes simulated hardware and software, and acts as a real-world object.


"""


