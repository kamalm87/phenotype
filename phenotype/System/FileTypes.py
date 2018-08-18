if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))

from enum              import auto
from States.Properties import FlagProperty
from Func.Aggregator   import IOR
from Core.Auxiliary    import Apply

class FileCategories(object):
    ''' '''
    Audio = set([
        'alac',
        'ape',
        'flac',
        'm4a',
        'mp3',
        'ogg',
        ])
    Code = set([
        'c',
        'cpp',
        'h',
        'js',
        'py',
        'vim'
        ])
    Image = set([
        'png',
        'jpg',
        'jpeg'
        ])
    Meta = set([
        'json',
        'xml'
        ])
    Tabular = set([
        'csv' 
        ])
    @classmethod
    def __lookup__(cls, item):
        ''' '''
        return item.lower()
    @classmethod
    def __factory__(cls):
        ''' '''
        def build_lookup_category(bag):
            return LookupCategory( cls.__lookup__, *bag)
        return build_lookup_category
    @classmethod
    def __iter__(cls):
        ''' '''
        lookup_categories = List.Mapped(cls.__factory__(), cls.Audio, cls.Code, cls.Image, cls.Meta, cls.Tabular)
        yield from lookup_categories
class FileTypes(FlagProperty):
    ''' '''
    Audio = auto(); Code = auto(); Image = auto(); Meta = auto(); Tabular = auto();
    @classmethod
    def __map__(cls):
        ''' '''
        return LookupMapping( *zip( FileCategories.__iter__(), cls ) )
    @classmethod
    def FromExtension(cls, extension):
        ''' '''
        return IOR( *cls.__map__()[extension.Format] )
