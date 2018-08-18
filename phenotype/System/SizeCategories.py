if __name__ == '__main__':
    from sys       import path    as __sys_path__
    from os.path   import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from Func.Ranges import AnchorFirst as __anchor_first__
from operator import __pow__
from enum import Enum
class SizeCategories(Enum):
    __limits__ = list(__anchor_first__.Until(__pow__,1024,7))
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
