from sys import path        as __sys_path__
from os.path import abspath as __abs_path__
__sys_path__.insert(0, __abs_path__('..'))
from operator    import ( 
    attrgetter   as __op_attr_getter__,
    itemgetter   as __op_item_getter__,
    methodcaller as __op_method_caller__,
    eq           as __op_eq__,
    )
