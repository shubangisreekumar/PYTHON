n=int(input("Enter number of lines: "))
for i in range(1,n+1):
    for k in range(1,i+1):
        pat=k*i
        print(pat,end=" ")
    print(" ")
