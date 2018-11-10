#my code
if __name__ == '__main__':
    s = input()

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
    # print(s.isalnum())
    for char in range(len(s)):
        if s[char].isalnum():
            print(True)
            break
        elif char+1 == len(s) and not(s[char].isalnum()):
            print(False)
# In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
    # print(s.isalpha())
    for char in range(len(s)):
        if s[char].isalpha():
            print(True)
            break
        elif char+1 == len(s) and not(s[char].isalpha()):
            print(False)

# In the third line, print True if  has any digits. Otherwise, print False. 
    for char in range(len(s)):
        if s[char].isdigit():
            print(True)
            break
        elif char+1 == len(s) and not(s[char].isdigit()):
            print(False)
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
    for char in range(len(s)):
        if s[char].islower():
            print(True)
            break
        elif char+1 == len(s) and not(s[char].islower()):
            print(False)
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    for char in range(len(s)):
        if s[char].isupper():
            print(True)
            break
        elif char+1 == len(s) and not(s[char].isupper()):
            print(False)

#btter code:
# if __name__ == '__main__':
    # s = input()

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
    print(any(str.isalnum(c) for c in s))
# In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
    print(any(str.isalpha(c) for c in s))
# In the third line, print True if  has any digits. Otherwise, print False. 
    print(any(str.isdigit(c) for c in s))
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
    print(any(str.islower(c) for c in s))
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    print(any(str.isupper(c) for c in s))


#better code:
# I see eval as a hacky solution. eval should only ever be used with caution and there's usually a
# better solution. It's fragile (you may accidentally create invalid code) and can be dangerous 
# (can offer ways for malicious code to be injected). It's also significantly slower, because the 
# python code created by eval has to be recompiled on every iteration.

# You can do this more cleanly and safely a couple of ways. You could use getattr(). But I prefer 
# just using function references. Remember that class methods are just functions with an object as
#  the first parameter - true in any OO language but directly visible and usable from Python.

for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print any(method(c) for c in s)