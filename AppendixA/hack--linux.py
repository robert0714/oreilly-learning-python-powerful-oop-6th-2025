#!/usr/bin/python3
import sys
print(sys.platform)

for i in range(5):
    print('👍' * (i + 1))

if sys.platform.startswith('linux'):    # for clicks
    input('Press enter to close')
