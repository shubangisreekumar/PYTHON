word=input("Enter a word: ")
words=list(word)
first_letter=word[0]
length=len(word)
for i in range(1,length):
    if(words[i]==first_letter):
        words[i]='$'
word="".join(words)
print(word)
