names = ['ljy' , 'way' ,'wzh']
message0 = f"尊敬的{names[0]},我诚挚的邀请你共进晚餐"
print(message0)
message1 = f"尊敬的{names[1]},我诚挚的邀请你共进晚餐"
print(message1)
message2 = f"尊敬的{names[2]},我诚挚的邀请你共进晚餐"
print(message2)

print("way临时有事来不了")
del names[1]
names.append('lx')
message0 = f"尊敬的{names[0]},我诚挚的邀请你共进晚餐"
message1 = f"尊敬的{names[1]},我诚挚的邀请你共进晚餐"
message2 = f"尊敬的{names[2]},我诚挚的邀请你共进晚餐"
print(message0)
print(message1)
print(message2)

