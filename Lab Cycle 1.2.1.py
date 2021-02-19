sentence="Its a copy of a copy of a copy"
counts = dict()
words = sentence.split()
for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:
        counts[word]=1
print(counts)
