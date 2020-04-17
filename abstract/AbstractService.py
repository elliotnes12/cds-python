from abc import ABCMeta, abstractmethod

class AbstractService:
    __metaclass__ = ABCMeta

    """
      call dynamic function
    """
    def init(self,args = None): 
        getattr(self,args['actionMethod'])(args)