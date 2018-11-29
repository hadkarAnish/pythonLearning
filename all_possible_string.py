#minion game
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

#my code - inefficient as 3 for loops
def minion_game(string):
    vowels = ['A','E','I','O','U']
    c_count = 0
    v_count = 0
    for current_letter in range(len(string)):
        if string[current_letter] in vowels:
            for v in range(current_letter,len(string)):
                v_count += 1
        else:
            for c in range(current_letter,len(string)):
                c_count += 1
    if c_count > v_count:
        print('Stuart',c_count)
    elif c_count == v_count:
        print('Draw')
    elif c_count < v_count:
        print('Kevin',v_count)

if __name__ == '__main__':
    s = input()
    minion_game(s)

#better code 
# def minion_game(string):
#     vowels = ['A','E','I','O','U']
#     c_count = 0
#     v_count = 0
#     for current_letter in range(len(string)):
#         if string[current_letter] in vowels:
#             v_count += (len(string)-current_letter)
#         else:
#             c_count += (len(string)-current_letter)
#     if c_count > v_count:
#         print('Stuart',c_count)
#     elif c_count == v_count:
#         print('Draw')
#     elif c_count < v_count:
#         print('Kevin',v_count)

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)