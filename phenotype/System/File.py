from Core       import (
    Accumulator,
    Evaluator,
    List,
    LookupCategory,
    LookupMapping,
    NamedTuple,
    Reducer,
    )
from Dates      import DateTime
from os         import stat, listdir, walk
from os.path    import (
    abspath,
    basename,
    dirname,
    exists,
    isdir,
    isfile,
    islink,
    ismount,
    splitext,
    join,
    )
from enum       import auto, Enum
from Properties import FlagProperty


class SizeCategories(Enum):
    __limits__ = [ 1 * 1024 ** i for i in range(7)  ]
    Bytes = 0; KiloBytes = 1; MegaBytes = 2; GigaBytes = 3; TeraBytes = 4; PetaBytes = 5;
    @property
    def Multipler(self):
        ''' '''
        return self.__limits__[self.value]
    @property
    def Short(self):
        ''' '''
        return str().join( filter(str.isupper, self.name) )
    @classmethod
    def __grouped__(cls):
        ''' '''
        return { e.value : e for e in iter(cls) }
    @classmethod
    def __getitem__(cls, value):
        ''' '''
        return cls.__grouped__().get(value)
    @classmethod
    def FindCategory(cls, byte_value):
        maximum_category = len(cls.__limits__)-1
        for index, value in enumerate(cls.__limits__):
            if byte_value <= value:
                index = index - 1 if index else index 
                return cls.__grouped__()[index]
        return cls.__grouped__()[maximum_category]
class PathType(FlagProperty):
    ''' '''
    Exists = auto(); Directory = auto(); File = auto(); Link = auto(); Mount = auto(); Null = auto(); 
    __evaluator__ = Evaluator(exists, isdir, isfile, islink, ismount, )
    @classmethod
    def FromFilePath(cls, file_path):
        ''' '''
        pairs   = zip( cls.__evaluator__(file_path), cls )
        results = (prop for cond,prop in pairs if cond)
        return cls.Accumulate(*results) or cls.Null
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
        return cls.Accumulate ( *cls.__map__()[extension.Format] )
class FileSize(NamedTuple):
    __slots__ = ('Bytes', 'Category')
    def __init__(self, byte_size):
        ''' '''
        self.Bytes    = byte_size
        self.Category = SizeCategories.FindCategory(byte_size)
    @property
    def Human(self):
        ''' '''
        size = round(self.Bytes / self.Category.Multipler, 2)
        short = self.Category.Short
        return f'{size} {short}'
    def __str__(self):
        ''' '''
        return f'{self.Human}'
    def __lt__(self, other):
        ''' '''
        return self.Bytes < other.Bytes
    def __eq__(self, other):
        ''' '''
        return self.Bytes == other.Bytes
    def __add__(self, other):
        ''' '''
        return self.Bytes + other.Bytes
class Time(NamedTuple):
    ''' '''
    __slots__ = ('Access','Modified')
    def __init__(self, access, modified):
        ''' '''
        self.Access   = DateTime.FromTimeStamp(access)
        self.Modified = DateTime.FromTimeStamp(modified)
    def __lt__(self, other):
        ''' '''
        return self.Modified < other.Modified
    def __eq__(self, other):
        ''' '''
        return self.Modified == other.Modified
class Id(NamedTuple):
    ''' '''
    __slots__ = ('User', 'Group')
    def __init__(self, user, group):
        ''' '''
        self.User  = user
        self.Group = group
    def __eq__(self, other):
        ''' '''
        return self.User == other.User and self.Group == other.Group
    def __hash__(self):
        ''' '''
        return hash((self.User, self.Group))
class MetaData(NamedTuple):
    ''' '''
    __slots__ = ('Size','Time', 'Id', 'Type')
    def __init__(self, file_path):
        ''' '''
        sr     = stat(file_path)
        self.Size = FileSize(sr.st_size)
        self.Time = Time(sr.st_atime, sr.st_mtime)
        self.Id   = Id(sr.st_uid, sr.st_gid)
        self.Type = PathType.FromFilePath(file_path)
    def __str__(self):
        ''' '''
        return f'{self.Size} {self.Time.Modified}'
class Extension(NamedTuple):
    ''' '''
    __slots__ = ( 'Name', 'Raw', 'Format', 'Types' )
    def __init__(self, file_path):
        ''' '''
        items    = splitext(file_path)
        self.Name   = items[0]
        self.Raw    = items[-1]
        self.Format = self.Raw[1:]
        self.Types  = FileTypes.FromExtension(self)
    def __str__(self):
        ''' '''
        if self.Types:
            return f'{self.Format}\t{self.Types.name}'
        else:
            return self.Format
class File(NamedTuple):
    __slots__ = ('Path', 'Name','Directory','MetaData','Extension')
    def __init__(self, file_path):
        ''' '''
        self.Path      = abspath(file_path)
        self.Name      = basename(self.Path)
        self.Directory = dirname(self.Path)
        self.MetaData  = MetaData(self.Path)
        self.Extension = Extension(self.Path)
    def __str__(self):
        ''' '''
        return f'{self.Name}\t{self.MetaData}\t{self.Extension}'
    #2 CONTEXT
    def __enter__(self, mode='rt'):
        ''' '''
        return open(self.Path, mode)
    def __exit__(self, exc_type, exc_value, traceback):
        ''' '''
        pass
    @classmethod
    def FromDirectory(cls, directory_path):
        ''' '''
        paths = List.Mapped( lambda p : join(directory_path,p), *listdir(directory_path) )
        return List.Mapped(File, *paths)

if __name__ == '__main__':
    Files = File.FromDirectory('/home/k/yt/data/yt-albums/')
    f = Files[0]
    print(f)
