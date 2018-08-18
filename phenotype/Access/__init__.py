#! /usr/bin/python
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
# from sys import path        as __sys_path__
# from os.path import abspath as __abs_path__
# __sys_path__.insert(0, __abs_path__('..'))
#
from operator import ( 
    attrgetter   as __op_attr_getter__,
    itemgetter   as __op_item_getter__,
    methodcaller as __op_method_caller__,
    eq           as __op_eq__,
    )
from collections   import deque as __deque__
from itertools     import (
    dropwhile   as __drop_while__,
    islice      as __islice__,
    zip_longest as __zip_longest__,
    filterfalse as __filter_false__,
    )
from phenotype.Core.Get         import ( 
    Item as _item_access,
    Name as _name_access, )
from phenotype.Core.Incrementer import Incrementer as __INCREMENTER__
from phenotype.Func.Partials    import ( 
    Head      as _fn_head,
    Tail      as _fn_tail,
    Reduction as _fn_reduce,)
