#! /usr/bin/python
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
from collections.abc import Callable as __abc_callable__
from functools import ( 
    reduce         as __func_reduce__,
    partial        as __func_partial__,
    update_wrapper as __func_update_wrapper__,
    )
from itertools import (
    starmap     as __it_starmap__,
    filterfalse as __it_filter_false__,
    dropwhile   as __it_drop_while__,
    takewhile   as __it_take_while__,
    zip_longest as __it_zip_longest__,
    repeat      as  __it_repeat__,
    )
from operator import (
    eq as __op_eq__,
    __ior__,
    __imul__,
    __isub__,
    __iadd__,
    __concat__,
    __itruediv__,
    )
