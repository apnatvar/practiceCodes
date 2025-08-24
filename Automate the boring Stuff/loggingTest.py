import logging

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s') # logs to console
logging.basicConfig(filename='loggingTestLog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s') # logs to filename


# logging.disable(logging.CRITICAL) # will disable loggin
# you can switch loggin on and off with a single command
# is better than using print statements all the time

## LOG LEVELS
# debug (lowest  )
# info
# warning
# error
# critical (highest)

logging.debug('Start' +str(5) +'of program')

def factorial(n):
    logging.debug('Called function factorial with value n= '+str(n))
    total = 1
    for i in range(n+1):
        total *= i
        logging.critical('Running multiplication loop with value i= '+str(i)+ ' and total= '+str(total))
    return total

factorial(10)

logging.debug('End of program')

