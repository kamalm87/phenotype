from datetime import timedelta as __dt_time_delta__
from math     import floor     as __math_floor__
class Duration(object):
    ''' '''
    __slots__ = '_time_delta'
    days          = property( lambda self : self._time_delta.days )
    seconds       = property( lambda self : self._time_delta.seconds )
    total_seconds = property( lambda self : self._time_delta.total_seconds )

    @property
    def minutes(self):
        ''' '''
        return __math_floor__( self.total_minutes )
    @property
    def total_minutes(self):
        ''' '''
        return self._time_delta.seconds / 60
    @property
    def total_hours(self):
        ''' '''
        return self.total_minutes / 60
    @property
    def hours(self):
        ''' '''
        return __math_floor__( self.total_hours )
    def __init__(self, seconds=0, microseconds=0):
        ''' '''
        self._time_delta = __dt_time_delta__(seconds=seconds,microseconds=microseconds)
    def __repr__(self):
        ''' '''
        rep = str(self._time_delta)
        if not self.hours:
            return ':'.join(rep.split(':')[1:])
        else:
            return rep
    def __lt__(self, val):
        ''' '''
        return self._time_delta < val
    def __le__(self, val):
        ''' '''
        return self._time_delta <= val
    def __eq__(self, val):
        ''' '''
        return self._time_delta < val
    def __ge__(self, val):
        ''' '''
        return self._time_delta <= val
    def __gt__(self, val):
        ''' '''
        return self._time_delta < val
