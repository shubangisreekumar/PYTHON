word=input("Enter the word: ")
vowels_list=[]
vowels =['a','e','i','o','u']
for i in word:
    if(i in vowels and i not in vowels_list):
        vowels_list.append(i)
print("Vowels in the list: ")
print(vowels_list)
