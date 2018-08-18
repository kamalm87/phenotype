if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from States.Date import Months as __date_months__

class _fn:
    Values  = staticmethod( lambda d : set( filter(None,d.values()) ) )
    CharSet = staticmethod( lambda x,y: set(map(chr,range(x,x+y))))

class Characters:
    ''' '''
    Empty     = r''
    Space     = r' '
    Tab       = r'\t'
    Digit     = r'\d'
    NewLine   = r'\n'
    Letter    = r'\w'
    NonLetter = r'\W'
class Alpha:
    ''' '''
    Lower = _fn.CharSet(97,26)
    Upper = _fn.CharSet(65,26)
    Letters = Lower.union(Upper)

class Dates:
    ''' '''
    class Months:
        ''' '''
        Names = _fn.Values(__date_months__.Names)
        Abbrs = _fn.Values(__date_months__.Abbrs)
