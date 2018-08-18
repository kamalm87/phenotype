if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from Func.Partials import ( Reduction as __func_reduce__ )
from calendar  import (
    calendar   as __cal_calendar__,
    month_name as __cal_month_name__,
    month_abbr as __cal_month_abbr__,
    monthrange as __cal_monthrange__,
    )
class _fn:
    ''' '''
    EnumDict = staticmethod( __func_reduce__( enumerate, dict ) )
class Months(object):
    ''' '''
    Names = _fn.EnumDict( __cal_month_name__ )
    Abbrs = _fn.EnumDict( __cal_month_abbr__ )
