from fractions import Fraction
import time

firstx = 0
firsty = 0
secondx = 0
secondy = 0
print('Slope with 2 points calculator made by Lexzach')
print('')
print('READY')
print('')
while True: 
    print('X1')
    firstx = input()
    print('Y1')
    firsty = input()
    print('X2')
    secondx = input()
    print('Y2')
    secondy = input()
    print('')

    solveX = float(secondx) - float(firstx)
    solveY = float(secondy) - float(firsty)
    solveAll = Fraction(solveY/solveX).limit_denominator(1000)

    time.sleep(0.5)
    print('Answer:')
    print(solveAll)
    print('')
    print('READY')
    print('')
    time.sleep(1.5)
