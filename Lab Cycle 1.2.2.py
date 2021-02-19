integer_list=[]
result=[]
n=int(input("Enter the number of elements in the list: "))
print("Enter Elements of the list")
for i in range(n):
    elements=int(input())
    integer_list.append(elements)
for i in integer_list:
    if(i>100):
        result.append('over')
    else:
        result.append(i)
print(result)
