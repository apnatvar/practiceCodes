def reachTargetSum(target, givenNumbers, added={}):#added helps in memoization
    #decreases time complexity from O(n^m * m) to O(n * m^2)
    #space complexity remains the same O(m^2)
    if (target in added):
        return added[target]
    if (target == 0):
        return []
    elif (target < 0):
        return None
    shortestArray = None
    for i in givenNumbers:
        returnedValue = reachTargetSum(target-i, givenNumbers, added)
        if (returnedValue != None):
            tempAnswer = returnedValue + [i] #combine the elements into a single list if it is not NoneS
            if (shortestArray == None or len(tempAnswer) < len(shortestArray)):
                shortestArray = tempAnswer

    added[target] = shortestArray
    return added[target]

target = int(input("Enter target word\n"))
givenNumbers = list(map(int,input("\nEnter the substrings separating them by single space. Press return to end\n").strip().split()))
print(reachTargetSum(target,givenNumbers))
