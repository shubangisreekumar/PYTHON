for i in range(1000,8000,1):
   for k in range(32,100,1):
       if(i==k*k):
           element=str(i)
           if(int(element[0])%2 == 0 and int(element[1])%2 == 0 and int(element[2])%2 == 0 and int(element[3])%2 == 0):
               print(i)
