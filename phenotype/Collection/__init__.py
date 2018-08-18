from sys import path        as __sys_path__
from os.path import abspath as __abs_path__
__sys_path__.insert(0, __abs_path__('..'))

from operator import (methodcaller as __op_method_caller__)
from collections.abc import ( Callable as __abc_Callable__ )
