# entry = int(input("Insert your cents here: "))
entry = 12

quarters = 25
dimes = 10
nickels = 5
pennies = 1

set = set()

matriz = []

def makeChange():

    list = []

    order = [quarters,dimes,nickels,pennies]

    list.append(counter(entry,quarters))
    list.append(counter(num,dimes))
    list.append(counter(num,nickels))
    list.append(counter(num,pennies)) 

    matriz.append(list)

    set.update(list)


def counter(entry,coin):
    global num
    num = entry
    equal = num // coin

    if num // coin > 0 :
        num -= coin

    return(equal)

def addAll():
    pass

def contains(e):
    if e in set:
        return True
    else:
        return False

def equals(s):
    pass

def iterator():
    pass

def size():
    len(set)

def toArray():
    print(matriz)

makeChange()
toArray()