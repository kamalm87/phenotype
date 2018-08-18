from operator import ( methodcaller as __op_method_caller__ )

Items  = __op_method_caller__('items')
Keys   = __op_method_caller__('keys')
Values = __op_method_caller__('values')
def Create(name, *args, **kwargs): return __op_method_caller__(name, *args, **kwargs)
