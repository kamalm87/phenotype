from os.path import exists as __os_path_exists__
from json    import loads  as __json_load_string__
from Mapping import Mapping

class JsonMapping(Mapping):
    ''' Creates a dynamic class from a json file '''
    @staticmethod
    def __load__(text):
        ''' '''
        if __os_path_exists__(text):
            return __json_load_string__(open(text,'rt').read())
        else:
            raise Exception('TODO')
    def __init__(self, data):
        ''' '''
        super().__init__( self.__load__(data) )
