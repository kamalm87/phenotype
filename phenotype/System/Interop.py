if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from collections.abc import ( Callable as __abc_callable__ )
from shlex           import ( split    as __shlex_split__ )
from subprocess      import (
    call         as __sp_call__,
    check_call   as __sp_check_call__,
    check_output as __sp_check_output__,
    )
from Func.Partials   import (
    Head      as __func_reduce__,
    Reduction as __func_reduce__,
    Tail      as __func_tail__,
    )
from Access.Invoke import Create as __create_invoker__

class Parser(__abc_callable__):
    ''' '''
    Unicode = __func_tail__(str,'utf8')
    Split   = __create_invoker__('splitlines') 
    @classmethod
    def Sequence(cls, *processes, from_unicode=True, split_second=False, split_end=False):
        ''' '''
        sequence = [cls.Unicode] if from_unicode else []
        if split_second: sequence.append(cls.Split)
        sequence.extend(processes)
        if split_end: sequence.append(cls.Split)
        return cls( __func_reduce__(*sequence) )
    def __init__(self, process=__func_tail__(str,'utf8')):
        ''' '''
        self.process = process
    def __call__(self, result):
        ''' '''
        return self.process(result) if result else result
class Command(__abc_callable__):
    ''' '''
    def __init__(self, command_name, parser=Parser()):
        ''' '''
        self.command_name = command_name
        self.parser       = parser
    def __call__(self, *args):
        ''' '''
        args = [self.command_name] + __shlex_split__(' '.join(map(str,args)) )
        return self.parser(__sp_check_output__( args ))
