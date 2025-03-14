# Use in tools that don't handle text with Unicode emojis

import sys
print(sys.platform)

for i in range(5):
    print('\U0001F44D' * (i + 1))

if sys.platform.startswith('win'):    # for clicks
    input('Press enter to close')

