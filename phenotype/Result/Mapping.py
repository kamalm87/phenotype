from datetime import timedelta as __date_time_delta__
from re import findall as __re_find_all__

class Mapping:
    ''' Creates a dynamic class from a dictionary '''
    @classmethod
    def _normalize(cls, item):
        ''' '''
        text = __re_find_all__(r'[^_]+',item)
        return ''.join( map(str.capitalize, text))
    @classmethod
    def _get_time(cls, item):
        ''' '''
        return __date_time_delta__( seconds=int(item) )
    def __init__(self, mapping):
        ''' '''
        for field, item in mapping.items():
            setattr(self, self._normalize(field), item)
