first_names=['Ashton','Jade','kacey','Luke','Michael','Taylor','Calum']
i=0
for k in first_names:
    for n in k:
        if(n=='a' or n=='A'):
            i=i+1
print("Total number of 'a's in the list: ",i)
