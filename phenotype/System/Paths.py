if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from os.path import ( 
    abspath    as __os_path_abspath__,
    basename   as __os_path_basename__,
    curdir     as __os_path_curdir__,
    dirname    as __os_path_dirname__,
    exists     as __os_path_exists__,
    isdir      as __os_path_is_dir__,
    islink     as __os_path_is_link__,
    isfile     as __os_path_is_file__,
    ismount    as __os_path_is_mount__,
    splitext   as __os_path_split_ext__,
    expanduser as __os_path_expanduser__,
    expandvars as __os_path_expand_vars__,
    join       as __os_path_join__,
    )
from sys               import ( path as __sys_path__ )
from enum              import auto
from States.Properties import FlagProperty
from Func.Aggregator   import IOR
from Core.Auxiliary    import Apply

class Paths:
    ''' '''
    @classmethod
    def Abs(cls, var):
        ''' '''
        return __os_path_abspath__(dir_path)
    @classmethod
    def Base(cls, var):
        ''' '''
        return __os_path_basename__(var)
    @classmethod
    def Concat(cls, *paths):
        ''' '''
        return cls._AbsolutePath(__os_path_join__(*map(cls._Expand,paths)))
    @classmethod
    def Current(cls):
        ''' '''
        return cls.Abs(__os_path_curdir__)
    @classmethod
    def Dir(cls, var):
        ''' '''
        return __os_path_dirname__(var)
    @classmethod
    def Expand(cls, var):
        ''' '''
        return __os_path_expanduser__(__os_path_expand_vars__(var))
    @classmethod
    def Insert(cls, path, index=0):
        ''' '''
        __sys_path__( index, cls.Abs(path) )
class PathType(FlagProperty):
    ''' '''
    Exists = auto(); Directory = auto(); File = auto(); Link = auto(); Mount = auto(); Null = auto(); 
    __evaluator__ = Apply(__os_path_exists__, __os_path_is_dir__, __os_path_is_file__, __os_path_is_link__, __os_path_is_mount__, )
    @classmethod
    def FromFilePath(cls, file_path):
        ''' '''
        pairs   = zip( cls.__evaluator__(file_path), cls )
        results = (prop for cond,prop in pairs if cond)
        return IOR(*results) or cls.Null
