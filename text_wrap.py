import textwrap

def wrap(string, max_width):
    list1 = []
    list1 = list(string)
    list2 = []
    temp_string = ""
    for i in range(len(string)):
        if (i+1)%max_width!=0:
            temp_string=temp_string+list1.pop(0)
        else:
            temp_string=temp_string+list1.pop(0)
            temp_string=temp_string+" "
    list2 = temp_string.split(" ")
    for i in range(len(list2)):
        print(list2[i])
    return ''

#better code:
# return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

# if __name__ == '__main__':