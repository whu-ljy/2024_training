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

print("我现在又只能邀请两位嘉宾参加晚餐了")
a =names.pop()
print(f"亲爱的{a}，我很抱歉不能与你共进晚餐")
b = names.pop()
print(f"亲爱的{b}，我很抱歉不能与你共进晚餐")
c = names.pop()
print(f"亲爱的{c}，我很抱歉不能与你共进晚餐")
d = names.pop()
print(f"亲爱的{d}，我很抱歉不能与你共进晚餐")
print(f"亲爱的{names[0]}，记得今晚的晚餐")
print(f"亲爱的{names[1]}，记得今晚的晚餐")

del names[0]
del names[0]
print(names)
