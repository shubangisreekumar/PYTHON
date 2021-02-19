n=int(input("Enter the number of terms to be printed: "))
a=0
b=1
i=0
if(n<0):
    print("Enter positive number")
else:
    print("Fibonacci series upto",n)
    while(i<n):
        print(a)
        c=a+b
        a=b
        b=c
        i=i+1
