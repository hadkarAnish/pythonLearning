def print_formatted(number):
    num_width=number.bit_length()
    for i in range(1,number+1):
        print("{0:{w}} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=num_width))

#can use this hacky way cuz you remove the 0x part from the string output
# str(oct(i)[2:]).rjust(w,' ')

if __name__ == '__main__':