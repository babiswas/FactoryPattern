from abc import ABC,abstractmethod

class Body(ABC):
    
    @abstractmethod
    def assembly_engine(self):
        pass
    
    @abstractmethod
    def set_body_type(self):
        pass
    
