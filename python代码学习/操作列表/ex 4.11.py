pizza_list = ['a' , 'b' , 'c']
friend_pizza_list = pizza_list[:]
print(friend_pizza_list)
pizza_list.append('d')
friend_pizza_list.append('e')
print(f"我的批萨有{pizza_list}")
print(f"我好朋友的批萨有{friend_pizza_list}")