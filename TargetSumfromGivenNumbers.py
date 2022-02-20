def reachTargetSum(target, givenNumbers, added={}):#added is for memoization
    if (target in added):
        return added[target]
    if (target == 0):
        return True
    elif (target < 0):
        return False
    elif (givenNumbers == []):
        return False
    for i in givenNumbers:
        if (reachTargetSum(target-i,givenNumbers,added) == True):
            added[target] = True
            return added[target]
    added[target] = False
    return added[target]

#this code is limited by the minimum recursion depth
target = int(input("Enter target sum\n"))
givenNumbers = list(map(int,input("\nEnter the numbers separating them by single space. Press return to end\n ").strip().split()))
print(reachTargetSum(target,givenNumbers))
