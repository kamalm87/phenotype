# -*- coding: utf-8 -*-

"""Top-level package for phenotype."""

__author__ = """Kamal McDermott"""
__email__ = 'kamal.mcdermott@gmail.com'
__version__ = '0.1.0'

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
# __all__ = [ 'Access', 'Assignment', 'Func' ]
from sys import path        as __sys_path__
from os.path import abspath as __abs_path__
__sys_path__.insert(0, __abs_path__('.'))

# import phenotype.Access     as Access
# import phenotype.Assignment as Assignment
# import phenotype.Collection as Collection
# import phenotype.Core       as Core
# import phenotype.Func       as Func
# import phenotype.Interfaces as Interfaces
# import phenotype.Predicate  as Predicate
# import phenotype.Result     as Result
# import phenotype.States     as States
# import phenotype.System     as System
# import phenotype.Text       as Text
