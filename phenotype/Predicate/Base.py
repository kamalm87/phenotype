# if __name__ == '__main__':
from sys import path        as __sys_path__
from os.path import abspath as __abs_path__
__sys_path__.insert(0, __abs_path__('..'))

from operator       import __not__
from Core.Auxiliary import Apply as __func_apply__
from Func.Partials  import ( 
    Head      as __func_head__,
    Tail      as __func_tail__,
    Reduction as __func_reduce__, )

def Invert(predicate): return __func_reduce__(predicate,__not__)
def Never(*predicates): return __func_reduce__(__func_apply__(*predicates), any, __not__)
