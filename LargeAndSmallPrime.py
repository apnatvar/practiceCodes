import random

print("Enter 0 to print a small list of prime number in a range you need")
print("Enter 1 to print a random large prime number")
choice = 1#int(input())

def checkEven(number):
    if (number%2 == 0):
        return True
    return False

def checkWithOdd(number):
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if (number%i == 0):
            return True
    return False

def checkPrime(number):
    if (checkEven(number) and number != 2):
        return False
    if (checkWithOdd(number) and number != 3):
        return False
    return True

"""I have used the Miller Rabin Primality Test to speed up the process of checking through large random integers
For the actual algorithm please look up on Youtube or GeeksForGeeks"""
def checkLargePrime(number, iterations):
    if (number == 3):
        return True
    numberCopy = number - 1
    while (numberCopy%2 == 0):
        numberCopy = numberCopy // 2
    a = random.randint(2, number-1)
    b0 = pow(a, numberCopy, number)
    if (b0 == -1 or b0 == 1):
        return True
    bn = b0
    for _ in range(iterations):
        bn = (bn*bn)%number
        if (bn==number-1):
            return True
    return False


def optionA():
    print("Enter [start, end] to print a list")
    start = int(input("Enter Start of Range\n"))
    end = int(input("Enter End of Range\n"))
    print()
    for i in range(start,end+1):
        if checkPrime(i):
            print(i)

def optionB():
    bits = int(input("Enter the number of bits required in the prime\n"))
    complexity = 5
    inputNumber = int(random.getrandbits(bits))
    inputNumber |= (1 << bits - 1) | 1 #changes first and last bit to 1 so that the random number is always odd
    #this helps ensure that the number is alwasy 1024 bits
    #also saves on computation as any even number is obviously not prime.
    while not checkLargePrime(inputNumber, complexity):
        inputNumber = random.getrandbits(bits)
        inputNumber |= (1 << bits - 1) | 1
    print(inputNumber,"is probably prime.")

if choice == 1:
    optionB()
elif choice == 0:
    optionA()

