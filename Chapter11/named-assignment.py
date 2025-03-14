# Code from the book, with file opens added to make it runnable, 
# and numbers added to prints to denote examples.

F = 'lines.txt'
ignore = stop = 'stop\n'
print(0, repr(open(F).read()))


# Traditional

file = open(F)
line = file.readline()             # Sans the := expression 
if line:
    print(1, line)

file = open(F)
line = file.readline()             # Ditto, in while loops
while line:
    print(2, line)
    line = file.readline()


file = open(F)
while True:                        # Sans both := and redundancy
   line = file.readline()
   if not line: break
   print(3, line)


# Named assignment

file = open(F)
if line := file.readline():        # The := alternatives
    print(4, line)

file = open(F)
while line := file.readline():
    print(5, line)


file = open(F)
if (line := file.readline()) != ignore:        # Parentheses required
    print(6, line)

file = open(F)
while (line := file.readline()) != stop:       # And not a bad idea 
    print(7, line)
