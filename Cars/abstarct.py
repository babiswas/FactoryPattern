from abc import ABC,abstractmethod

class CarFactory(ABC):
    
    @abstractmethod
    def get_body(self):
        pass
    
    @abstractmethod
    def get_hardware(self):
        pass