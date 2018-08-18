from phenotype.Access import (
   _item_access    as __get_item__,
   _name_access    as __get_name__,
   __INCREMENTER__ as Incrementer,
   _fn_head        as Head,
   _fn_tail        as Tail,
   _fn_reduce      as Reduction,
    __drop_while__,
    __islice__,
    __zip_longest__,
    __filter_false__,
    __deque__,
    __op_eq__,
    )
class Iterable:
    ''' '''
    __SENTINEL__ = object()
    class _Head_Slice:
        ''' '''
        __slots__ = 'n'
        def __init__(self, n):
            ''' '''
            self.n        = n
        @property
        def __predicate__(self):
            ''' '''
            return Incrementer(self.n)
        def __call__(self, iterable):
            ''' '''
            yield from __drop_while__( self.__predicate__, iterable)
    class _Tail_Slice:
        ''' '''
        __slots__ = 'n'
        def __init__(self, n):
            ''' '''
            self.n = n
        def __call__(self, iterable):
            ''' '''
            dq = __deque__(iterable)
            while len(dq) > self.n:
                yield dq.popleft()
    @staticmethod
    def __islicer__(stop, start=None, step=None):
        ''' '''
        if not start:
            return Head( __islice__, stop )
        else:
            return Head( __islice__, start, stop, step)
    @classmethod
    def __pluck__(cls, iterable, default=None):
        ''' '''
        return next( iterable, default)
    @classmethod
    def __take_tail__(cls, n=1):
        ''' '''
        return Tail( __deque__, n )
    @classmethod
    def __offset__(cls, i=None, j=None):
        ''' '''
        if all((i, j)):
            slicer = Reduction( cls._Head_Slice(i), cls._Tail_Slice(j) )
        elif i:
            slicer = _Head(i)
        elif j:
            slicer = _Tail(j)
        else:
            slicer = iter
        return slicer
    @classmethod
    def Bucket(cls, n):
        ''' '''
        def _iterable_bucket(iterable):
            ''' '''
            return __zip_longest__( __repeat__(iter(iterable),n),  fillvalue=cls.__SENTINEL__)
        return _iterable_bucket
    @classmethod
    def Slicer(cls, i=None, j=None):
        ''' '''
        return cls.__offset__(i,j)
    @classmethod
    def PredicateSplit(cls, iterable, pred):
        ''' '''
        return tuple( fn(pred,titer)  for titer, fn in zip(__tee__(iterable),(__filter_false__,filter)) )
    @classmethod
    def Head(cls, items):
        ''' '''
        return Reduction( cls.__islicer__(1), cls.__pluck__ )
    @classmethod
    def Tail(cls, items):
        ''' '''
        return Reduction( __take_tail__(1), cls.__pluck__  )(items) 
    @classmethod
    def LessHead(cls, items):
        ''' '''
        return cls.__islicer__(None,1)(items)
    @staticmethod
    def LessTail(items):
        ''' '''
        return cls._Tail_Slice(1)(items)
    @classmethod
    def First(cls, key):
        ''' '''
        def _first(iterable):
            ''' '''
            return next( filter( Head(__op_eq__,  key), iterable), None )
        return _first
    @classmethod
    def Pick(cls,i):
        ''' '''
        def _pick(items): return next( cls.__islicer__(None,i)(items), None )
        def _rpick(items): return __get_item__(0)(cls.__take_tail__(abs(i))(items))
        return _pick if i >= 0 else _rpick
    @staticmethod
    def Take(i,j):
        ''' '''
        return __get_item__(slice(i,j))
    @staticmethod
    def Select(*indices):
        ''' '''
        return __get_item__(tuple(indices))
__doc__ = 'Sequential-like accessors for iterables'
