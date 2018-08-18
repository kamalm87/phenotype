if __name__ == '__main__':
    from sys     import ( path    as __sys_path__ )
    from os.path import ( abspath as __abs_path__ )
    __sys_path__.insert(0, __abs_path__('..'))

def Sequence(item): return not isinstance(item,str) and hasattr(item,'__iter__')
