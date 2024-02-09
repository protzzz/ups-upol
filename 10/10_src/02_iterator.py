# Iterátory

"""
>>> i = iter([1, 2, 3])
>>> next(i)
1
>>> next(i)
2
>>> next(i)
3
>>> next(i)
StopIteration
"""


# Více iterátorů:
"""
>>> arr = [1, 2, 3]
>>> i1 = iter(arr)
>>> i2 = iter(arr)
>>> next(i1)
1
>>> next(i2)
1
>>> next(i2)
2
>>> next(i1)
2
>>> next(i1)
3
>>> next(i1)
StopIteration
>>> next(i2)
3
>>> next(i2)

StopIteration
"""

# Iterátor je iterovatelná hodnota:

"""
>>> i = iter([1, 2, 3])
>>> i2 = iter(i)
>>> next(i)
1
>>> next(i2)
2
"""

# Řetězec je iterovatelná hodnota:

"""
>>> i = iter("python")
>>> next(i)
'p'
>>> next(i)
'y'
>>> next(i)
't'
>>> next(i)
'h'
>>> next(i)
'o'
>>> next(i)
'n'
>>> next(i)
StopIteration
"""

# Číselná posloupnost:

"""
>>> i = iter(range(3))
>>> next(i)
0
>>> next(i)
1
>>> next(i)
2
>>> next(i)
StopIteration
"""

# For cyklus:
"""
>>> for char in "python":
	print(char)

	
p
y
t
h
o
n
>>> i = iter([1, 2, 3])
>>> next(i)
1
>>> for x in i:
	print(x)

	
2
3
"""

# Seznam prvků posloupnosti:
"""
>>> list(range(3))
[0, 1, 2]
"""

# Otevřený textový soubor má řádky za prvky: 
"""
>>>> with open("file.txt") as file:
         for line in file:
            print(repr(line))

        
'line1\n'
'line2\n'
'line3\n'
"""


