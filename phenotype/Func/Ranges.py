from phenotype.Func import (
    __abc_callable__,
    __it_starmap__,
    __it_repeat__,
    __it_zip_longest__,)

class RangeParameter(__abc_callable__):
    ''' '''
    @staticmethod
    def __range__(*args):
        ''' '''
        return range(*args)
    def __init__(self, seed, stop=None, step=None):
        ''' '''
        self.seed, self.stop, self.step = seed, stop, step
    def __iter__(self):
        ''' '''
        yield from filter(None,(self.seed,self.stop,self.step))
    def __call__(self):
        ''' '''
        return self.__range__(*self)
    @classmethod
    def FromPlus(cls, start, plus, step=None):
        ''' '''
        return cls( start, start+plus,step)
class TabularParameters(__abc_callable__):
    ''' '''
    def __init__(self, anchor_value, first=True):
        ''' '''
        self.anchor_value = anchor_value
        self.first        = first
    def __call__(self, range_parameter):
        ''' '''
        anchor = __it_repeat__(self.anchor_value)
        rng    = range_parameter()
        return zip(anchor,rng) if self.first else zip(rng,anchor)

class _Anchor:
    @classmethod
    def _Invoke(cls, binary_fn, anchor, seed, stop=None, step=None):
        rp = RangeParameter(seed,stop,step)
        tp = cls._Anchor(anchor) 
        return __it_starmap__(binary_fn,tp(rp))
    @staticmethod
    def _Anchor(anchor):
        ''' '''
        raise NotImplementedError

    @classmethod
    def StartEnd(cls, binary_fn, start, end, step=None):
        ''' '''
        return cls._Invoke(binary_fn,start,end,step)
    @classmethod
    def Until(cls, binary_fn, anchor,end):
        ''' '''
        return cls._Invoke(binary_fn,anchor,end)
    @classmethod
    def StartPlus(cls, binary_fn, anchor, start, plus, step=None):
        ''' '''
        return cls._Invoke(binary_fn,anchor,start,start+plus,step)
class AnchorFirst(_Anchor):
    ''' '''
    @staticmethod
    def _Anchor(anchor):
        ''' '''
        return TabularParameters(anchor)
class AnchorSecond(_Anchor):
    ''' '''
    @staticmethod
    def _Anchor(anchor):
        ''' '''
        return TabularParameters(anchor, False)
