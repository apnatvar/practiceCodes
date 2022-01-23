inputString = input("Enter String to remove duplicates from\n")
modifiedInputString = ""
for char in inputString:
    if char not in modifiedInputString:
        modifiedInputString = modifiedInputString + char
print(modifiedInputString)
