def fibonacci(num, explored={}):#explored is a dictionary which helps in memoization
    #this program uses memoization to speed up the calculation
    #without this the program would explore 2^n nodes whereas now it explored 2n nodes
    #This brings the time complexity down to O(n) from O(n^2)
    #IT also increases the space complexity from 1 to O(n)
    if (num in explored):
        return explored[num]
    if (num < 3):
        return 1
    else :
        explored[num] = fibonacci(num-1,explored) + fibonacci(num-2, explored)
        return explored[num]

n = int(input("Enter the nth number in the fibonacci series you want\nThe series starts 0,1,1,2..... with 0 being the first\n"))

print(fibonacci(n))

#this program is limited to the maximum recursion depth. #Use loop if you want a number higher in the sequence than 998
