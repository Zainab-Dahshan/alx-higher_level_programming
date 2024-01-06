#!/usr/bin/python3
import sys
# Import sys module which provides access to some variables used
# or maintained by Python interpreter

import hidden_4 as hidden
# Import a module named 'hidden_4' and alias it as 'hidden'

if __name__ != "__main__":
# Check if the script is being run directly or being imported
    exit()
    # If the script is being imported, exit the script immediately

for name in dir(hidden):
# Start a loop over each attribute in the 'hidden' module
    if name[0:2] != "__":
    # If the attribute name doesn't start with '__' (meaning it's not
    # a special method or attribute), print its name
        print(name)
