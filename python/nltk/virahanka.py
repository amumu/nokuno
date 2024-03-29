# Natural Language Toolkit: code_virahanka

def virahanka1(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["S"]
    else:
        s = ["S" + prosody for prosody in virahanka1(n-1)]
        l = ["L" + prosody for prosody in virahanka1(n-2)]
        return s + l

def virahanka2(n):
    lookup = [[""], ["S"]]
    for i in range(n-1):
        s = ["S" + prosody for prosody in lookup[i+1]]
        l = ["L" + prosody for prosody in lookup[i]]
        lookup.append(s + l)
    return lookup[n]

def virahanka3(n, lookup={0:[""], 1:["S"]}):
    if n not in lookup:
        s = ["S" + prosody for prosody in virahanka3(n-1)]
        l = ["L" + prosody for prosody in virahanka3(n-2)]
        lookup[n] = s + l
    return lookup[n]

from nltk import memoize
@memoize
def virahanka4(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["S"]
    else:
        s = ["S" + prosody for prosody in virahanka4(n-1)]
        l = ["L" + prosody for prosody in virahanka4(n-2)]
        return s + l

if __name__ == '__main__':
    print virahanka1(4)
    print virahanka2(4)
    print virahanka3(4)
    print virahanka4(4)

    from time import *
    print "virahanka1"
    t = time()
    virahanka1(31)
    print time() - t

    t = time()
    print "virahanka2"
    virahanka2(31)
    print time() - t

    t = time()
    print "virahanka3"
    virahanka3(31)
    print time() - t

    t = time()
    print "virahanka4"
    virahanka4(31)
    print time() - t

