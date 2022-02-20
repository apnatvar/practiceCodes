def travelling(m, n, travelled={}):#travelled is a dictionary used for memoization
    #speeds up the code, decreseasing time complexity from O(2^n+m) to O(m*n)
    #the space complexity remains the same: O(m+n)
    key = str(m) + ':' + str(n);
    if (key in travelled):
        return travelled[key]
    if (m == 1 and n == 1):
        return 1
    elif (m==0 and n==0):
        return 0
    elif (m==0 or n==0):
        return 1
    travelled[key] = travelling(m-1, n, travelled) + travelling(m, n-1, travelled)
    return travelled[key]

print("Enter a grid to travel to in a M x N format. Starting grid is always 0 x 0")
m = int(input("Enter the value of m\n"))
n = int(input("Enter the value of n\n"))
print("The nummber of ways to read the last box in the grid is " + str(travelling(m,n)))
