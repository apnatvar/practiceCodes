a = [1,2,3,4,5,6,7,8,9,10]
result = 0
xor = a[0]
#an implementation of kadane's algorithm
for i in range(1,len(a)):
    xor = xor if xor^a[i]<xor else xor^a[i]
    result = xor if xor>result else result
    #result = 0 if result<0 else result

print(result)

