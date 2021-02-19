word=input("Enter a String: ")
words=list(word)
first_letter=words[0]
words[0]=words[-1]
words[-1]=first_letter
word="".join(words)
print(word)
