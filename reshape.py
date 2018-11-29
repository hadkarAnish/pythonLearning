import numpy
# Task

# You are given a space separated list of nine integers. Your task is to convert this list into a 3X3
#  NumPy array.


n = numpy.array(list(map(int,input().split())))

print(numpy.reshape(n,(3,3)))

