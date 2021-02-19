dict1={"black":99,"Red":77,"Green":97}
dict2={"Grey":79,"Cherry-Red":17,"Teal":91}
print("The First Dictionary: ",dict1)
print("The Second Dictionary: ",dict2)
d=dict1.copy()
d.update(dict2)
print("The Merged Dictionary: ",d)
