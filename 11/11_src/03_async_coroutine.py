# Asynchronní korutiny
import aio

"""
>>> c1 = aio.sleep(1)
>>> aio.run(c1)
### vteřina čekání
"""
async def print_now(string):
    print(string)

"""
>>> c2 = print_now("A")
>>> aio.run(c2)
A
"""
    
async def print_after(delay, string):
    await aio.sleep(delay)
    print(string)

"""
>>> c3 = print_after(1, "A")
>>> aio.run(c3)
### vteřina čekání
A
"""

async def prog1():
    await print_after(2, "A")
    await print_after(2, "B")
    print("C")

"""
>>> aio.run(prog1())
### dvě vteřiny čekání
A
### dvě vteřiny čekání
B
C
"""



async def prog2():
    promise1 = aio.arun(print_after(2, "A"))
    promise2 = aio.arun(print_after(2, "B"))
    await promise1
    await promise2
    print("C")

"""
>>> aio.run(prog2())
### dvě vteřiny čekání
A
B
C
"""

# Následující dva příklady s nekonečnem nespouštějte v IDLE.
# Vše zablokuje:
async def infinite(i):
    while True:
        print(i)
    
async def infinite_task(): 
    promise1 = aio.arun(infinite(1))
    promise2 = aio.arun(infinite(2))
    print(3)
    await promise1
    await promise2
    

"""
>>> aio.run(infinite_task())
"""

# Umožní prokládání korutin:
async def infinite2(i):
    while True:
        print(i)
        await aio.sleep(0)
    
async def infinite_task2(): 
    promise1 = aio.arun(infinite2(1))
    promise2 = aio.arun(infinite2(2))
    print(3)
    await promise1
    await promise2
    
"""
>>> aio.run(infinite_task2())
"""

async def return_after(delay, value):
    await aio.sleep(delay)
    return value

"""
>>> aio.run(return_after(1, 5))
### vteřina čekání
5
"""

async def add_after(delay, x, y):
    promise1 = aio.arun(return_after(delay, x))
    promise2 = aio.arun(return_after(delay, y))
    return (await promise1) + (await promise2)

"""
>>> aio.run(add_after(3, 4, 5))
### tři vteřiny čekání
9
"""
