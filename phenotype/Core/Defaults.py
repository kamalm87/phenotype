class Nullable(object):
    ''' '''
    def __init__(self): pass
    def __getitem__(self, i): return self
    def __call__(self, *args, **kwargs): return self
    def __repr__(self): return ''
    def __str__(self): return ''
    def __bool__(self): return False
    def __getattr__(self, key): return self
    def __eq__(self, val): return val is None
