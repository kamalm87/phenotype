if __name__ == '__main__':
    from sys       import path        as __sys_path__
    from os.path   import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from .Instance import Instance as __Instance__
from .Partials import Reduction


#1 GENERIC
class Invoker:
    ''' '''
    Instances = __Instance__()
    def __init__(self, cls):
        ''' '''
        if cls not in self.Instances:
            self.Instances.add(cls)
        self._instance = self.Instances[cls]
    def __call__(cls, *args):
        ''' '''
        return cls._instance.__call__(*args)
    @classmethod
    def __reduction__(cls, sequence, initial=None):
        ''' '''
        return Reduction.Reduce(initial, *sequence)
    @classmethod
    def __reducer__(cls, sequence):
        ''' '''
        return Reduction(*sequence)
    @classmethod
    def Default(cls, wrapped_result=None):
        ''' '''
        def _wrapped_result(*args, **kwargs): return wrapped_result
        return _wrapped_result
    def __getattr__(self, name):
        ''' '''
        return self.__dict__[name] if name in self.__dict__ else getattr(self._instance,name,None)
