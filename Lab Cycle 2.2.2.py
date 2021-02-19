n=int(input("Enter the number of words to be entered: "))
word_list=[]
print("Enter words: ")
for i in range(n):
    word=input()
    word_list.append(word);
max_len=len(word_list[0])
longest=word_list[0]
for k in word_list:
    if(len(k) > max_len):
        max_len=len(k)
        longest=k
print("Longest word is",longest,"with length",max_len)
