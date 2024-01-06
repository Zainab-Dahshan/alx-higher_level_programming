#!/usr/bin/python3
import sys
# Import the sys module which provides access to some variables
# used or maintained by the Python interpreter
if __name__ != "__main__":
    exit()
# Check if the script is being run directly or being imported
argc = len(sys.argv) - 1

i = 0
result = 0
for arg in sys.argv:
    if i != 0:
        result += int(arg)
    else:
        i += 1
print("{:d}".format(result))
