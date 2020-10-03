import time
import subprocess
from fractions import Fraction
copytoclipboard = False

print("Slope-Intercept Calculator With Single Point")
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
    if xcoord > ycoord and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        subanswer = xcoord - ycoord
    if ycoord > xcoord and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        subanswer = ycoord - xcoord
    if ycoord == xcoord and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        subanswer = 0
    if ycoord > xcoord and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        if str(ycoord) != str(0):
            xcoord = xcoord * -1
            subanswer = xcoord + ycoord
        else:
            ycoord = ycoord * -1
            subanswer = xcoord + ycoord
    if ycoord > xcoord and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        ycoord = ycoord * -1
        subanswer = xcoord + ycoord
    if ycoord > xcoord and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        ycoord = ycoord * -1
        subanswer = xcoord + ycoord
    if xcoord > ycoord and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        xcoord = xcoord * -1
        subanswer = xcoord + ycoord
    if xcoord > ycoord and str(xcoord) != str(xcoord.replace("-", "")) and str(ycoord) == str(ycoord.replace("-", "")):
        if str(ycoord) != str(0):
            ycoord = ycoord * -1
            subanswer = xcoord + ycoord
        else:
            xcoord = xcoord * -1
            subanswer = xcoord + ycoord
    if xcoord > ycoord and str(xcoord) == str(xcoord.replace("-", "")) and str(ycoord) != str(ycoord.replace("-", "")):
        xcoord = xcoord * -1
        subanswer = xcoord + ycoord

    time.sleep(0.5)
    if int(subanswer) >= 0:
        print("Answer: " + "y=" + str(slope) + "x+" + str(subanswer))
        if copytoclipboard == True:
            clipboard("y=" + str(slope) + "x+" + str(subanswer))
    else:
        print("Answer: " + "y=" + str(slope) + "x" + str(subanswer))
        if copytoclipboard == True:
            clipboard("y=" + str(slope) + "x" + str(subanswer))
    