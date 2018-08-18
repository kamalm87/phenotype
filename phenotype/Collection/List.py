class List(list):
    ''' '''
    def __init__(self, *items):
        ''' '''
        super(List,self).__init__(iter(items))
    def __call__(self, function):
        '''Maps a function to all items in List, returning List'''
        for index, item in enumerate(self): self[index] = function(item)
        return self
    def filter(self, predicate=None):
        ''' '''
        self = self.__init__( *filter(predicate, self) )
    def Extended(self, *items):
        super().extend(*items)
        return self
    def Filtered(self, predicate=None):
        ''' '''
        return List( *filter(predicate, self) )
    def On(self, function):
        ''' '''
        return function(self)
