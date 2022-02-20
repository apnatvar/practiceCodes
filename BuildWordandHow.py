def reachWord(word, wordList, added={}):
    if (word in added):
        return added[word]
    elif (word == ''):
        return [[]]
    collect = []
    for i in wordList:
        if (word.find(i) == 0):
            slicedWord = word[len(i):]
            temp = reachWord(slicedWord, wordList, added)
            for j in temp:
                collect.append([i]+j)
    added[word] = collect
    return collect
word = input("Enter target word\n")
wordList = list(map(str,input("\nEnter the substring separating them by single space. Press return to end\n").strip().split()))
p = set()
for i in reachWord(word, wordList):
    p.add(tuple(i))
for i in p:
    print(list(i))
