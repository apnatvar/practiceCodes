N = 9
A = [5, 6, 7, 8, 9, 10, 1, 2]
#A = [3, 5, 1, 2]

keys = [k for k in range(11)]

def search(start, end):
    if (start <= end):
        mid = (start + end) // 2
        if (A[mid] == key):
            return mid
            #quit()
        elif (A[mid] > key):
            return search(start, mid-1)
        else:
            return search(mid+1, end)
    else:
        x = -1
        return x

i = 0
for _ in range(0,len(A)):
    if (A[i] > A[i+1]):
        break
    i = i + 1
#print("i -",i)

for key in keys:
    if (key >= A[0]):
        print(key, "-",search(0, i))
    elif (key <= A[-1]):
        print(key, "-",search(i, len(A)))
    else:
        print(key, "- -1")
