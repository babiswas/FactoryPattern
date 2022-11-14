from Cars.Hardware.abstract import Hardware


class StandardHardware(Hardware):
    
    def put_console(self):
        super().put_console()
        print("Small screen with digital speedometer:")
        
    
    def assembly_seats(self):
        super().assembly_seats()
        print("Normal Fabric:")
        
        


class LuxuryHardware(Hardware):
    
    def put_console(self):
        super().put_console()
        print("Big screen with analog speedometer:")
        
    
    def assembly_seats(self):
        super().assembly_seats()
        print("Leather Fabric:")