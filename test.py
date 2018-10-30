#!/usr/bin/env python

# Imported subprocess calls an executable and stores what that executable sends to stdout in a variable
import subprocess
p = subprocess.Popen(["./hello.py"], shell=False, stdout=subprocess.PIPE)
output = p.stdout.read()


# rstrip() method clear all characters from the end of the string. We have blank line that needs to be removed
print(output.rstrip())

# Comparing between both outputs. If they are the same - test will pass!
if  output.rstrip() == 'hello':
        print("Test is passed")
else:
        print("Test is failed")
