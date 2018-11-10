# My code
def count_substring(string, sub_string):
    # list1 = list(string)
    # list2 = list(sub_string)
    count = 0
    # for char in range(len(string)):
        # if sub_string == string[char:char+len(sub_string)]:
            # count += 1
#my code but 1 liner
    return sum([1 for char in range(len(string)) if sub_string == string[char:char+len(sub_string)]])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)