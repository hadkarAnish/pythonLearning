A = 0
B = 1


class AnishAdd:

    def output(self, x, y):
        # There is really no need for us to create these 3 variables, instead can use A + B directly in print, but this was an eg for
        # global vars with inheritance that is why used these
        z = x + y
        print(str(z))


class CallingAnish(AnishAdd):

    def inputs(self):
        global A, B
        A = int(input("enter a number: "))
        B = int(input("enter another number: "))


add1 = CallingAnish()
add1.inputs()
add1.output(A, B)
