from phenotype.Access import __op_method_caller__ as __INVOKER__
__doc__ = 'Common extension methods invokers'
Items  = __INVOKER__('items')
Keys   = __INVOKER__('keys')
Values = __INVOKER__('values')
def Create(name, *args, **kwargs): return __INVOKER__(name, *args, **kwargs)
