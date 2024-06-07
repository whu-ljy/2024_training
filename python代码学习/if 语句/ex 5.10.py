current_users = ['aaA','b','c','d','e']
new_users = ['Aaa','b','x','y','z']

current_users_fuben = []
for user in current_users:
    current_users_fuben.append(user.lower())

for user in new_users:
    if user.lower() in current_users_fuben:
        print("需要使用别的用户名")
    else:
        print("用户名未被使用")
