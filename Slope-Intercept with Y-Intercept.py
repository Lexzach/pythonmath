import time
import subprocess
from fractions import Fraction
copytoclipboard = False

print("Slope-Intercept Calculator")
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
    print("Enter Y-Intercept")
    yintercept = input()
    print("")
    if str(slope) == str(slope.replace("/-", "")):
        slope = Fraction(slope).limit_denominator(1000)

    time.sleep(0.5)
    if int(yintercept) >= 0:
        print("Answer: " + "y=" + str(slope) + "x+" + yintercept)
        if copytoclipboard == True:
            clipboard("y=" + str(slope) + "x+" + yintercept)
    else:
        print("Answer: " + "y=" + str(slope) + "x" + yintercept)
        if copytoclipboard == True:
            clipboard("y=" + str(slope) + "x" + yintercept)