"""


Topic: PIP in Python

======================================================================
                              PIP
======================================================================

Definition:
- PIP is The Package Manager for Python You Can Install a Module(library) on Your Systems
- PIP is Python's package installer. It is used to install,upgrade, and remove Python packages from the Python Package Index
  (PyPI) and other package repositories.
  


PIP stands for:
PIP = Pip Installs Packages

======================================================================
                         COMMON COMMANDS
======================================================================

#Install a package:
    pip install package_name

#Upgrade a package:
    pip install --upgrade package_name

#Uninstall a package:
    pip uninstall package_name

#Check installed packages:
    pip list

#Show package information:
    pip show package_name

#Check PIP version:
    pip --version

======================================================================
                           SIMPLE EXAMPLE
======================================================================

Example:
Install the requests package from the terminal:

    pip install requests

Then use it in Python:

"""

import requests

print("Requests version:", requests.__version__)


"""
======================================================================
                         QUICK REVISION
======================================================================

pip install package
-> Install a package

pip uninstall package
-> Remove a package

pip list
-> Show installed packages

pip show package
-> Show package information

pip --version
-> Show PIP version


"""
