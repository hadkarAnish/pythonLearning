if __name__ == '__main__':
    N = int(input())

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# input().split()
# print(a,b,c)
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

arr = []
for i in range(N):
    input_1 = input().split(' ')
    command = input_1.pop(0)
    if command == 'insert':
        eval("arr.{0}({1}, {2})".format(command, input_1[0], input_1[1]))
    elif command == 'print':
        print(arr)
    elif command == 'remove' or command == 'append':
        eval("arr.{0}({1})".format(command, input_1[0]))
    else: 
        eval("arr.{0}()".format(command))


#### better solution
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l