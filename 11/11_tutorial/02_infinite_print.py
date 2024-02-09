import aio

    
async def print_infinite(delay, string):
    while True:
        await aio.sleep(delay)
        print(string)

"""
>>> aio.run(print_infinite(1, "A"))
### čekání jednu vteřinu
A
### čekání jednu vteřinu
A
### čekání jednu vteřinu
A
...
"""

async def inf_print():
    promise1 = aio.arun(print_infinite(1, "A"))
    promise2 = aio.arun(print_infinite(2, "B"))
    await promise1
    await promise2

"""
>>> aio.run(inf_print())
### čekání jednu vteřinu
A
### čekání jednu vteřinu
B
A
### čekání jednu vteřinu
A
### čekání jednu vteřinu
B
A
### čekání jednu vteřinu
A
### čekání jednu vteřinu
B
A
...
"""
