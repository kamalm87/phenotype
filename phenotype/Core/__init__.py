#! /usr/bin/python
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
from collections.abc import ( Callable as __abc_callable__ )
from functools import ( partial as __ft_partial__ )
from itertools import ( 
    repeat as __it_repeat__,
    )
from operator import (
    __iadd__,
    __lt__,
    truth      as __op_truth__,
    attrgetter as __op_attr_getter__,
    itemgetter as __op_item_getter__,
    )
from phenotype.Assignment.Branch import Branch as __pt_branch__
from phenotype.Core.Auxiliary import ( 
    Apply     as __apply__,
    Identity  as __identity__,
    ReturnAs  as __return_as__,
    TryExcept as __try_except__,)
from phenotype.Core.Defaults     import Nullable
