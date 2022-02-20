def countWays(word, wordList, added={}):
    if (word == ''):
        return 1
    count = 0
    for i in wordList:
        if (word.find(i) == 0):
            slicedWord = word[len(i):]
            count = count + countWays(slicedWord, wordList, added)
    added[word] = count;
    return added[word]

word = input("Enter target word\n")
wordList = list(map(str,input("\nEnter the substring separating them by single space. Press return to end\n ").strip().split()))
print(countWays(word,wordList))
