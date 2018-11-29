#merge the tools

# The first line contains a single string denoting s. 
# The second line contains an integer, k, denoting the length of each subsegment.
S, N = input(), int(input()) 
# Sample Input

# AABCAAADA
# 3   
# Sample Output

# AB
# CA
# AD
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

# ❶iter(s) returns an iterator for S.

# ❷[iter(s)]*n makes a list of n times the same iterator for s.

# Example: [[iter(s)]*3] = ([iter(s), iter(s), iter(s)])

# ADVICE: It's not three copies of the same iterator, it's three times the same iterator object. Really:

# for part in zip(*[iter(S)] * N):
# It is equivalent to:

# it = iter(s)
# for part in zip(it, it, it):
# ❹*[] unpack a list:

# Example: print(*[1,2,3,4]) = print(1,2,3,4)

# ❺zip make an iterator that aggregates elements from each of the iterables.

# Example:

# >>>x = [1, 2, 3]
# >>> y = [4, 5, 6]
# >>> zipped = zip(x, y)
# >>> list(zipped)
# [(1, 4), (2, 5), (3, 6)]
# we have:

# zip(*[iter(s)]*3)
# It is equivalent to:

# itr = iter(s)
# zip(itr, itr, itr)
# it extracts an item from all the three iterators from the list in order. Since all the iterators are the same object, it just groups the list in chunks of 3.

# Example:

# for part in zip(*[iter('abcdefghi')]*3):
# 	print(part)
# a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i  a,b,c,d,e,f,g,h,i
# ^                    ^                    ^             
#       ^                    ^                    ^
#             ^                    ^                    ^
# Output:

# (a,b,c)

# (d,e,f)

# (g,h,i)

# iter explanation
# Approach 1 : Simply passing a list

# >>>s='abcdefghi'
# >>>zip(s, s, s)
# [('a', 'a', 'a'), ('b', 'b', 'b'), ('c', 'c', 'c'), ('d', 'd', 'd'), ('e', 'e', 'e'), ('f', 'f', 'f'), ('g', 'g', 'g'), ('h', 'h', 'h'), ('i', 'i', 'i')]
# Explaination: Simply combining the elements of the same index. The total number of elements is equal to the length of smallest list. Since list is same and has 9 elements, therefore there are 9 tuples.

# Approach 2 : Passing an interator of the list

# >>>s='abdefghi'
# >>>i=iter(s)
# >>>zip(i, i, i)
# [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
# Explaination : When passing iterators, zip internally invokes the next on the subsequent passed iterators before combining them. Since here, the iterator is to the same list. Hence you get such an output. For example,

# Output of (a, b, c) comes out like this:

# >>next(i) # first iterator passed
# a
# >>next(i) # second iterator passed
# b
# >>next(i) # third iterator passed
# c
# Combine them => (a,b,c)

# While generating the second tuple, (d, e, f)

# >>next(i) # Again on the fist iterator, last element 'c'
# d
# >>next(i) # Again on second iterator
# e
# >>next(i) # Again on third iterator
# f