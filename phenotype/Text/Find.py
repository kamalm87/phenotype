if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from re              import search as __re_search__, I as __re__I__, sub as __re_sub__
from functools       import wraps as __func_wraps__
from Func.Partials   import Reduction as __func_reduce__, Tail as __func_tail__
from Func.Aggregator import IOR as __IOR_AGG__
from Constants import Characters 

class RegexResult(object):
    ''' '''
    __slots__ = '_match'
    def __init__(self, match ):
        ''' '''
        self._match = match
    def __bool__(self):
        ''' '''
        return self._match is not None and bool(self._match)
    def __getitem__(self, group):
        ''' '''
        if not self:
            return ''
        if isinstance(group,int):
            return self._match.group(group)
        elif isinstance(group,slice):
            ''' '''
            return self._match.groups()[group]
    def __len__(self):
        ''' '''
        if self:
            return self.End - self.Start
        else:
            return 0
    def __repr__(self):
        ''' '''
        return self.First
    @property
    def First(self):
        ''' '''
        return self._match[0] if self else ''
    @property
    def Last(self):
        ''' '''
        if not self:
            return ''
        else:
            count = self.Count
            return self._match[count] if count else self.First
    @property
    def Count(self):
        ''' '''
        return self._match.lastindex or 0 if self else 0
    @property
    def Start(self):
        ''' '''
        return self._match.start() if self else None
    @property
    def End(self):
        ''' '''
        return self._match.end() if self else None

class Text:
    ''' '''
    __flags__         = [ __re__I__ ]
    __default_flags__ = __IOR_AGG__(*__flags__)
    @staticmethod
    def __not_instance__(item,instance_type=str):
        return not isinstance(item,instance_type)
    @classmethod
    def Get(cls, item):
        ''' '''
        if item is not None:
            return str(item) if self.__not_instance__(item,str) else item
        else:
            return str()
    @classmethod
    def Search(cls, pattern, flags=__default_flags__):
        ''' '''
        @__func_wraps__(__re_search__)
        def _find(text, flags=flags): return RegexFind(__re_search__(pattern, cls.Get(text), flags=flags))
        return _find
    @classmethod
    def Match(cls, pattern, flags=__default_flags__):
        ''' '''
        @__func_wraps__(__re_search__)
        def _find(text, flags=flags): return cls.Search(pattern, flags=flags)(text).First
        return _find
    @classmethod
    def Replace(cls, pattern, replacement=Characters.Empty, flags=__default_flags__):
        ''' '''
        @__func_wraps__(__re_sub__)
        def _replace(text, flags=flags): return __re_sub__( pattern, replacement, cls.Get(text), flags=flags)
        return _replace
    @classmethod
    def ReplaceWith( cls, *patterns, replacement=Characters.Empty, flags=__default_flags__):
        ''' '''
        return __func_reduce__( *map( __func_tail__( cls.Replace, replacement, flags), patterns) )
    @classmethod
    def ReplaceWithPairs(cls, *pattern_replacements, flags=__default_flags__):
        ''' '''
        replacements = ( cls.Replace(pattern,replacement,flags) for pattern, replacement in pattern_replacements )
        return __func_reduce__( *replacements )
