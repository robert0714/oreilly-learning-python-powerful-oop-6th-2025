class MyError(Exception): pass

def stuff(file):
    file.write('Hello?')             # May be delayed in file buffer
   #raise MyError()                  # <= Enable or disable me with a #

if __name__ == '__main__':
    file = open('temp.txt', 'w')     # Open an output file (this can fail too)
    try:
        stuff(file)                  # Raises exception
    finally:
        file.close()                 # Always close file to flush output buffers
    print('Am I reached?')           # Continue here only if no exception

