dictionary={"Green":15,"Red":13,"Blue":10,"Yellow":6}
print("The Dictionary: ",dictionary)
dictionary_list=list(dictionary.items())
print("The List: ",dictionary_list)
dictionary_list.sort()
print("Ascending Order: ",dictionary_list)
dictionary_list.sort(reverse=True)
print("descending Order: ",dictionary_list)
