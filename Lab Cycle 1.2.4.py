first_list=[99,89,79,69,97]
second_list=[77,87,97,67,97]
if(len(first_list)==len(second_list)):
    print("a. Both the lists are of the same length")
else:
    print("a. Both the lists are not of the same length")
if(sum(first_list)==sum(second_list)):
    print("b. The Sum of both the lists are equal")
else:
    print("b. The Sum of both the lists are not equal")
output=any(value in first_list for value in second_list)
if(output==True):
    print("c. Common elements in both lists",set(first_list).intersection(second_list))
else:
    print("c. There are no common elements in both lists")
