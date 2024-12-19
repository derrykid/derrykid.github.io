#!/usr/bin/env python3

# This script demonstrate how you can run linux commands in python
import time

# use subprocess module instead of os because
# 1. os module pass the full string
# 2. subprocess module pass a list and arguments ['ls', '-la']
# 3. it allows us to pass in characters like ', ", /...
import subprocess

# it will print the output to console directly
subprocess.run(['ls', '-la'])

time.sleep(3)

# We also can pass string by add a flag
subprocess.run(['ls -la ~'], shell=True)

time.sleep(3)

# catch the output to a variable
x = subprocess.run(['ls', '-la', '/'], capture_output=True)
out_string = x.stdout.decode()
print(out_string)
