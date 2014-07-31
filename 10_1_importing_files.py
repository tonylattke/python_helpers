##################### Importing file with name start with a number ######################

file_imported = __import__('10_0_importing_files')

t = file_imported.Person()

################################ Import and use modules #################################

## Option 1

import importing_files_class

t = importing_files_class.Human()

## Option 2 - Import and rename the module

import importing_files_class as MyTestLibrary

t = MyTestLibrary.Human()

## Option 3 - Import Class and don't need use module name

from importing_files_class import Human # [,other]

t = Human()

## Option 4 - Import everything and don't need use module name too

from importing_files_class import *

t = Human()