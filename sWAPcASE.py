def swap_case(s):
    a = []
    for i in range(len(s)):
        if(ord(s[i]) < 97 and ord(s[i]) >= 65) :
            # print(chr(ord(s[i])+32))
            a.append(chr(ord(s[i])+32))
            # s.replace(s[i],chr(ord(s[i])+32));
            # s[i] = chr(ord(s[i])+32);
        elif (ord(s[i]) >= 97 and ord(s[i]) < 129):
            # print(chr(ord(s[i])-32))
            a.append(chr(ord(s[i])-32))
            # s.replace(s[i],chr(ord(s[i])-32));
            # s[i] = chr(ord(s[i])-32);
        else:
            a.append(s[i])
    return str(''.join(a))

if __name__ == '__main__':

#shorter
print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])

#even shorter using inbuilt fn:
print("".join(map(str.swapcase, input())))

#shortest
return s.swapcase()