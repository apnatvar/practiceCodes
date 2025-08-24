import traceback
try:
    raise Exception('This is an error message.')
except:
    errorFile = open('errorLog.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('traceback info written to error log')


x = input("Enter e for error\n")
if x == 'e':
    raise Exception('You Entered e')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol must be a single character")
    if width < 2
        raise Exception("width must be greater than 2")
    if height < 2:
        raise Exception("height must be greater than 2")
    print(symbol*width)
    for i in range(height-2):
        print(symbol + (' '* (width-2)) + symbol)
    print(symbol*width)

boxPrint(x,5,4)


market2nd = {'ns':'green','ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market2nd)
switchLights(market2nd)
print(market2nd)
