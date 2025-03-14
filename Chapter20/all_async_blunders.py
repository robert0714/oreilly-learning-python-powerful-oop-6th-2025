import time, asyncio
def now(): 
    return time.strftime('[%H:%M:%S]')      # Local time, as hour:minute:second

async def producer(label):                     # await requires async
    await asyncio.sleep(2)                     # Call awaitable sleep
    return f'All done, {label}, {now()}'       # Result of await expression

async def main():
    print(producer('xxx'))

main()

"""
Users/me/Documents/t.py:14: RuntimeWarning: coroutine 'main' was never awaited
"""
print('-'*40)



async def main():
    print(producer('xxx'))

asyncio.run(main())                            


"""
<coroutine object producer at 0x10142e740>
/Users/me/Documents/t.py:22: RuntimeWarning: coroutine 'producer' was never awaited
"""
print('-'*40)



async def main():
    print('Start =>', now())
    print(await producer('xxx'))
    print(await producer('yyy'))
    print('Stop  =>', now())

asyncio.run(main())                            


"""
Start => [14:47:14]
All done, xxx, [14:47:16]
All done, yyy, [14:47:18]
Stop  => [14:47:18]
"""
print('-'*40)



async def main():
    print('Start =>', now())
    p1 = producer('xxx')
    p2 = producer('yyy')
    print('Await =>', now())
    print(await p1)
    print(await p2)
    print('Stop  =>', now())

asyncio.run(main())                            


"""
Start => [15:31:56]
Await => [15:31:56]
All done, xxx, [15:31:58]
All done, yyy, [15:32:00]
Stop  => [15:32:00]
"""




# Oter protocol demos not in the book...
"""
>>> async def p(): return 99
... 
>>> x = p()
>>> y = x.__await__()
>>> next(y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration: 99


>>> async def p():
...     yield 77
... 
>>> x = p()
>>> y = x.__await__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'async_generator' object has no attribute '__await__'. Did you mean: '__anext__'?


>>> async def p():
...     yield 77
... 
>>> x = p()
>>> y = x.__anext__()
>>> next(y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration: 77


>> async def p():
...    return 99    # await is not required
... 
>>> async def m():
...     print(await p())
... 
>>> asyncio.run(m())
99
"""
