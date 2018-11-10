#mine
def mutate_string(string, position, character):
    s = list(string)
    s[position] = character;
    s = ''.join(s)
    return s

# better
# def mutate_string(string, position, character):
#     list2=list(string)
#     list2[position]=character      
#     return ''.join(list2)
#1 liner
#def mutate_string(string, position, character):
#    return string[:position] + character + string[position + 1:]