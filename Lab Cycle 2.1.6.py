word=input("Enter a String: ")
word_dict={}
for i in word:
    if(i in word_dict):
        word_dict[i]=word_dict[i]+1
    else:
        word_dict[i]=1
print(word_dict)
