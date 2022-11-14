from Cars.cars import FamilyCar
from Cars.cars import OutdoorCar


def test_assembly_engine_family_car():
    f=FamilyCar()
    rbody=f.get_body()
    str1=rbody.assembly_engine()
    assert str1 == "1.2 Motor"
    

def test_body_type_family_car():
    f=FamilyCar()
    rbody=f.get_body()
    str1=rbody.set_body_type()
    assert str1 == "Pick Up"
    
    
def test_assembly_engine_sport_car():
    o=OutdoorCar()
    sbody=o.get_body()
    str1=sbody.assembly_engine()
    assert str1=="1.2 Motor"
    
def test_body_type_sport_car():
    o=OutdoorCar()
    sbody=o.get_body()
    str1=sbody.set_body_type()
    assert str1=="Pick up"
    
    
    