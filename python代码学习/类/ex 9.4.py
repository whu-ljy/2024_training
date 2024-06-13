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

A = Restaurant('麦当劳','快餐')
A.set_number_served(100)
print(f"{A.number_served}")

A.increment_number_served(9)
print(f"{A.number_served}")