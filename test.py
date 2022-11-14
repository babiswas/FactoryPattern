from Cars.cars import FamilyCar,OutdoorCar,BachelorCar,WealthyCar


def prepare_order(customer):
    factories={"Family":FamilyCar(),"Outdoor":OutdoorCar(),"Bachelor":BachelorCar(),"Wealthy":WealthyCar()}
    car=factories.get(customer)
    body_car=car.get_body()
    hardware_car=car.get_hardware()
    body_car.assembly_engine()
    body_car.set_body_type()
    hardware_car.put_console()
    hardware_car.assembly_seats()
    
if __name__=="__main__":
    order_list=["Family","Outdoor","Bachelor","Wealthy"]
    for order in order_list:
        print("=================================")
        prepare_order(order)
        print("=================================")
    