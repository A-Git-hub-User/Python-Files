# Just a quick script before bed.

# Importing "os" allows a line of code to reset the script, importing time will allow us to delay lines of code
import os
import sys
import time

# Functions are great! Use them more! -PyDev
def restart():
    print("Restarting...")
    time.sleep(5)
    os.execv(sys.executable, ['python'] + sys.argv)
    
x = int(input("\nEnter a number: "))
y = int(input("Enter another number: "))
# Removing useless code. -Pydev
print(x+y)

a = input("Do you want to restart the program? ")
if a in [ "yes", "y" ]: # if a == "yes" wont work.
    restart()
    # I don't know why you tried to import your own file??? -PyDev
elif a in [ "no", "n" ]:
    print("Ending the program...")
else:
    print("Invalid input. Ending the program...")
