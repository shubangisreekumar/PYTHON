number_list=[]
square_list=[]
n=int(input("Enter the number of elements in the list: "))
print("Enter the elements of the list: ")
for i in range(n):
    elements=int(input())
    number_list.append(elements)
for num in number_list:
    sq=num*num
    square_list.append(sq)
print("Square of the number in the list: ")
print(square_list)
