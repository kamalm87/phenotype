from operator  import eq      as __op_eq__
from functools import ( 
    partial        as __ft_partial__,
    update_wrapper as __ft_update_wrapper__,
    reduce         as __ft_reduce__,
    )
from sys       import path        as __sys_path__
from os.path   import abspath as __abs_path__
__sys_path__.insert(0, __abs_path__('..'))
