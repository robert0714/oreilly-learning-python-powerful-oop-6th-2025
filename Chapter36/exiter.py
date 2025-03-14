import sys

def bye():
    sys.exit(62)           # Crucial error: abort now!

try:
    bye()
except:
    print('Got it')        # Oops--we ignored the exit

print('Continuing...')

