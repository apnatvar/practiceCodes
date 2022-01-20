"""this is a basic hash function
This can hash multible strings such as names for your hash table
This is a weighted hash function i.e. will give different hash values for anagrams
If you wish to remove this comment out "++mul"
"""
def hashThisString(sample, hashVal, offset):
	mul = 1
	wordHash = 0
	for i in sample:
		basicHash = (ord(i) * mul + offset) % hashVal
		wordHash = wordHash + basicHash
		++mul #comment me out to convert this into a non-weighted hashing function
		print(" ",i," ",basicHash)#prints hashed value of each character
		#this is not necessary to print, you can comment this part out too

	wordHash = (wordHash + mul) % hashVal #adding the number of characters for further difference in hashing of the string
	return wordHash

maxHashVal = int(input("Enter the total number of slots in your hash table\n"))
offsetInput = int(input("Enter a offset value (Could be 0 as well)\n"))
inputString = input("\nEnter strings to display their hashed values based on a simple hashing function\nEnter END to stop the input function\n")
inputStrings = []
while (inputString != "END"):
	inputStrings.append(inputString)
	inputString = input("Enter Next String or END\n")


for strings in inputStrings:
	print("The Input String will be hashed as ",hashThisString(strings, maxHashVal, offsetInput))
