from Cars.Body.abstarct import Body


class RegularBody(Body):
    
    def assembly_engine(self):
        super().assembly_engine()
        print("1.2 Motor")
    
    
    def set_body_type(self):
        super().set_body_type()
        print("Pick Up")
        
        

class SportBody(Body):
    
    def assembly_engine(self):
        super().assembly_engine()
        print("1.2 Motor")
    
    
    def set_body_type(self):
        super().set_body_type()
        print("Pick Up")
        
        
        

