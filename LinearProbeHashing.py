"""This is a basic string hash function
Uses Linear Probing to return only unique hash values
if the number of strings is greater than the slots in the hash table, the program will prompty exit"""

stored = [] #keeps track of the used hash values

def hashThisStringUsingLinearProbing(sample, hashVal, offset):
    mul = 1
    wordHash = 0
    if (len(stored) == hashVal):
        print("Hash Table Full. Exiting Program.")
        quit()
    for i in sample:
        basicHash = (ord(i) * mul + offset) % hashVal
        wordHash = wordHash + basicHash
        ++mul #comment me out to convert this into a non-weighted hashing function
        print(" ",i," ",basicHash)#prints hashed value of each character
        #this is not necessary to print, you can comment this part out too
    wordHash = (wordHash + mul) % hashVal #adding the number of characters for further difference in hashing of the string
    while wordHash in stored:
        wordHash = (wordHash+1) % hashVal
    stored.append(wordHash)
    return wordHash

maxHashVal = int(input("Enter the total number of slots in your hash table\n"))
offsetInput = int(input("Enter a offset value (Could be 0 as well)\n"))
inputString = input("\nEnter strings to display their hashed values based on hashing function which uses Linear Probing\nEnter END to stop the input function\n")
inputStrings = []
while (inputString != "END"):
    inputStrings.append(inputString)
    inputString = input("Enter Next String or END\n")

for strings in inputStrings:
    print("The Input String will be hashed as ",hashThisStringUsingLinearProbing(strings, maxHashVal, offsetInput))
