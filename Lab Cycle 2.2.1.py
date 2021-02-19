word=input("Enter a word: ")
if(word[-3:]=='ing' or word[-3:]=='ING'):
    result=word+'ly'
    print(result)
else:
    result=word+'ing'
    print(result)
