if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from Access.Iterable import Iterable as __get_iter__
from Access.Item     import Names    as __get_names__

class __external__:
    ''' '''
    Names  = __get_names__.Get
    Slicer = __get_iter__.Slicer
class IterableProperty(property):
    ''' '''
    _instance = None
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        ''' '''
        super().__init__( fget, fset, fdel, doc )
    def __get__(self, instance, owner=None):
        ''' '''
        self._iterable = instance
        return self
    def __call__(self, iterable):
        ''' '''
        return self.__instance_type__(iterable)
    def __iter__(self):
        ''' '''
        yield from self._iterable
    def __getattr__(self, name):
        ''' '''
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            return self(map(__get_names__.Get(name), self))
    def __getitem__(self, key):
        ''' '''
        if isinstance(key,int):
            slicer = __get_iter__.Pick(key)
        elif isinstance(key,slice):
            slicer = __get_iter__.Slicer( key.start, key.end)
        else:
            slicer = None
        if slicer:
            return slicer(self._iterable)
    @property
    def __instance_type__(self):
        ''' '''
        return type(self._instance)

class SequenceProperty(IterableProperty):
    ''' '''
    def __getitem__(self, key):
        ''' '''
        return self._iterable[key]
class _Morpher(IterableProperty):
    ''' '''
    def Map(self, function):
        ''' '''
        for item in self._iterable:
            item = function(item)
class _Converter(IterableProperty):
    ''' '''
    @property
    def __iterable__(self):
        ''' '''
        return self._iterable
    def __wrap__(self, method):
        ''' '''
        def _wrap_method():
            return method(self._iterable)
        return _wrap_method
    def __init__(self, *methods):
        ''' '''
        super().__init__()
        for method in methods:
            setattr(self, method.__name__, self.__wrap__(method))


class On(property):
    ''' '''
    def __init__(self, arg):
        ''' '''
        super().__init__(fget=arg)
    def __get__(self, instance, owner=None):
        ''' '''
        return instance.__context__(self.fget)
class Context(type):
    ''' '''
    def __new__(cls, **key_words):
        ''' '''
        props = { }
        for k,v in key_words.items():
            props[k] = On(v)
        context_prop = type('Context',(property,),props)
        context_prop.__get__ = cls.__get__
        return context_prop(fget=cls.__context_on_link__  )
    def __get__(self, instance, owner=None):
        ''' '''
        self.__context__ = self.fget(instance)
        return self
    @staticmethod
    def __context_on_link__(instance):
        ''' '''
        def _context(container_type): return instance.__build__(container_type)
        return _context
