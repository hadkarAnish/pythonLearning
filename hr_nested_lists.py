# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#Input Format

#The first line contains an integer, , the number of students. 
#The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    second_lowest = sorted(list(set(score for name, score in arr)))[1]
    for a, b in sorted(arr):
        if b == second_lowest:
            print(a)
    # print('\n'.join([a for a,b in sorted(arr) if b == second_lowest]))
