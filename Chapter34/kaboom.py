def kaboom(x, y):
    print(x + y)                        # Trigger TypeError

def serve(n=2):                         # Simulate long-running task
    for i in range(n):
        try:
            kaboom([1, 2], 'hack')
        except TypeError:               # Catch and recover here
            print('Hello world!')
        print('Resuming here...')       # Continue here if exception or not

if __name__ == '__main__': serve() 

