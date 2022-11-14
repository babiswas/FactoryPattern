from abc import ABC,abstractmethod

class Hardware(ABC):
    
    @abstractmethod
    def put_console(self):
        pass
    
    @abstractmethod
    def assembly_seats(self):
        pass
    