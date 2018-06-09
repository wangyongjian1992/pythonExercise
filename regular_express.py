#!/usr/bin/python

import re
import random

m = re.match('foo', 'ofoo') # match begins at the begin of the string
if m is not None:
    print m.group()
else:
    print 'Nothing matched in match!'

m = re.search('foo', 'ofoo') # search is searching in the whole string
if m is not None:
    print m.group()
else:
    print 'Nothing matched in search!'

# generate a ip address and use the regular express to check the validation of the ip address
addr = ''
for i in range(3):
    addr += str(random.randint(0,255)) + '.'
addr += str(random.randint(0,255))
print addr

pattern2 = '((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)'
m = re.match(pattern2, addr)
if m is not None:
    print m.group()
