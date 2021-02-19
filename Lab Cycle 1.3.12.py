integer_list=[]
odd_list=[]
n=int(input("Enter the number of elements in the list: "))
print("Enter the elements of the list: ")
for i in range(n):
    elements=int(input())
    integer_list.append(elements)
for num in integer_list:
    if(num%2!=0):
        odd_list.append(num)
print("Result: ",odd_list)
