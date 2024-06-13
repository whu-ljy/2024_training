class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"餐馆名字是{self.restaurant_name} 餐馆类型是{self.cuisine_type}")

    def open_restaurant(self):
        print("working !")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,incre_number):
        self.number_served+=incre_number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_flavors(self):
        print(f"{self.flavors}")

A = IceCreamStand('AAA','BBB',['草莓','巧克力'])
A.show_flavors()
    
