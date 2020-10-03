import time
import subprocess
from fractions import Fraction
copytoclipboard = False

print("Slope-Intercept Calculator With Single Point")
print("CURRENTLY VERY UNSTABLE AND WILL GET WRONG ANSWERS")
print("")
print("Copy calculated value to clipboard automatically? (Y/N)")
if input() == "y":
    copytoclipboard = True
def clipboard(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
while True:
    print("")
    print("Enter Slope of the Line")
    slope = input()
    print("")
    print("Enter X")
    xcoord = input()
    print("Enter Y")
    ycoord = input()
    print("")
    if str(slope) == str(slope.replace("/-", "")):
        slope = Fraction(slope).limit_denominator(1000)
    if int(xcoord) > int(ycoord) and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        subanswer = int(xcoord) - int(ycoord)
        print("Debug: 1")
    if int(ycoord) > int(xcoord) and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        if int(ycoord) == int(slope):
            subanswer = xcoord
            print("Debug: 2a")
        else:
            subanswer = int(ycoord) - int(xcoord)
            print("Debug: 2b")
    if int(ycoord) == int(xcoord) and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        subanswer = 0
        print("Debug: 3")
    if int(ycoord) > int(xcoord) and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        if str(ycoord) != str(0):
            xcoord = int(xcoord) * -1
            subanswer = int(xcoord) + int(ycoord)
            print("Debug: 4a")
        else:
            ycoord = int(ycoord) * -1
            subanswer = int(xcoord) + str(ycoord)
            print("Debug: 4b")
    if int(ycoord) > int(xcoord) and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        ycoord = int(ycoord) * -1
        subanswer = int(xcoord) + int(ycoord)
        print("Debug: 5")
    if int(ycoord) > int(xcoord) and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        ycoord = int(ycoord) * -1
        subanswer = int(xcoord) + int(ycoord)
        print("Debug: 6")
    if int(xcoord) > int(ycoord) and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        xcoord = int(xcoord) * -1
        subanswer = int(xcoord) + int(ycoord)
        print("Debug: 7")
    if int(xcoord) > int(ycoord) and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        if str(ycoord) != str(0):
            ycoord = ycoord * -1
            subanswer = int(xcoord) + int(ycoord)
            print("Debug: 8")
        else:
            xcoord = int(xcoord) * -1
            subanswer = int(xcoord) + int(ycoord)
            print("Debug: 9")
    if int(xcoord) > int(ycoord) and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        xcoord = int(xcoord) * -1
        subanswer = int(xcoord) + int(ycoord)
        print("Debug: 10")
    if slope == 0:
        subanswer = ycoord
        print("Debug: 11")
    

    time.sleep(0.5)
    if int(subanswer) >= 0:
        print("Answer: " + "y=" + str(slope) + "x+" + str(subanswer))
        if copytoclipboard == True:
            clipboard("y=" + str(slope) + "x+" + str(subanswer))
    else:
        print("Answer: " + "y=" + str(slope) + "x" + str(subanswer))
        if copytoclipboard == True:
            clipboard("y=" + str(slope) + "x" + str(subanswer))
    