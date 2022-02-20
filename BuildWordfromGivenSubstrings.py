def reachWord(word, wordList, added={}):
    if (word in added):
        return added[word]
    elif (word == ''):
        return True
    for i in wordList:
        if (word.find(i) == 0):
            slicedWord = word[len(i):]
            x = reachWord(slicedWord, wordList, added)
            if (x == 1):
                added[word] = x
                return added[word]
    return False
word = input("Enter target word\n")
wordList = list(map(str,input("\nEnter the substring separating them by single space. Press return to end\n ").strip().split()))
print(reachWord(word,wordList))
