def reachTargetSum(target, givenNumbers, added={}):#added helps in memoization
    #decreases time complexity from O(n^m * m) to O(n * m^2)
    #increases space complexity from O(m) to O(m^2)
    if (target in added):
        return added[target]
    if (target == 0):
        return []
    elif (target < 0):
        return None
    for i in givenNumbers:
        returnedValue = reachTargetSum(target-i, givenNumbers, added)
        if (returnedValue != None):
            added[target] = returnedValue + [i] #combine the elements into a single list if it is not NoneS
            return added[target]
    added[target] = None
    return added[target]

target = int(input("Enter target sum\n"))
givenNumbers = list(map(int,input("\nEnter the numbers separating them by single space. Press return to end\n ").strip().split()))
print(reachTargetSum(target,givenNumbers))
