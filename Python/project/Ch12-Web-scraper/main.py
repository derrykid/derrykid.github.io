#! python
# stopwatch.py - A simple stopwatch program.
import subprocess
browser = subprocess.Popen('/usr/bin/midori')
print(browser.poll())
