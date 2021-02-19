integer_list=[]
positive_list=[]
n=int(input("Enter the number of elements in the list: "))
print("Enter the elements of the list: ")
for i in range(n):
    elements=int(input())
    integer_list.append(elements)
for num in integer_list:
    if(num>0):
        positive_list.append(num)
print("Positive Numbers: ")
print(positive_list)
