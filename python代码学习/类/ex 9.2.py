class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐馆名字是{self.restaurant_name} 餐馆类型是{self.cuisine_type}")

    def open_restaurant(self):
        print("working !")

A = Restaurant('川味坊','川菜')
B = Restaurant('半球山','西餐')
C = Restaurant('麦当劳','快餐')

A.describe_restaurant()
B.describe_restaurant()
C.describe_restaurant()