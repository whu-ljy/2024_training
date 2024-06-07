names = ['ljy' , 'way' ,'wzh']
message0 = f"尊敬的{names[0]},我诚挚的邀请你共进晚餐"
print(message0)
message1 = f"尊敬的{names[1]},我诚挚的邀请你共进晚餐"
print(message1)
message2 = f"尊敬的{names[2]},我诚挚的邀请你共进晚餐"
print(message2)

print("现在我找到了一个更大的餐桌 我可以多邀请三个人")
names.insert(0,'lx')
names.insert(2,'xyh')
names.append('xls')
print(f"尊敬的{names[0]},我诚挚的邀请你共进晚餐")
print(f"尊敬的{names[1]},我诚挚的邀请你共进晚餐")
print(f"尊敬的{names[2]},我诚挚的邀请你共进晚餐")
print(f"尊敬的{names[3]},我诚挚的邀请你共进晚餐")
print(f"尊敬的{names[4]},我诚挚的邀请你共进晚餐")
print(f"尊敬的{names[5]},我诚挚的邀请你共进晚餐")
print(f"我邀请了{len(names)}名嘉宾来共进晚餐")