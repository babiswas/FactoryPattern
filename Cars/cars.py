from Cars.abstarct import CarFactory
from Cars.Body.body import RegularBody,SportBody
from Cars.Hardware.hardware import StandardHardware,LuxuryHardware

class FamilyCar(CarFactory):
    
    def get_body(self):
        super().get_body()
        return RegularBody()
    
    def get_hardware(self):
        super().get_hardware()
        return StandardHardware()
    
    
class OutdoorCar(CarFactory):
    
    def get_body(self):
        super().get_body()
        return SportBody()
    
    def get_hardware(self):
        super().get_hardware()
        return StandardHardware()
    
    
class BachelorCar(CarFactory):
    
    def get_body(self):
        super().get_body()
        return RegularBody()
    
    def get_hardware(self):
        super().get_hardware()
        return LuxuryHardware()
    

class WealthyCar(CarFactory):
    
    def get_body(self):
        super().get_body()
        return SportBody()
    
    def get_hardware(self):
        super().get_hardware()
        return LuxuryHardware()
    