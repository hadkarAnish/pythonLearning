name, last_name = ['anish', 'hadkar']#, 'ajeet', 'wankhede']
print(name)
# this maps the first name and the last name only for anish and not for ajeet as the number of elements in the list
# shud be equal to the list of variables on the LHS


def drop_first_last_in_avg(grades):
    first_grade, *middle_grades, last_grade = grades
    avg = sum(middle_grades) / len(middle_grades)
    print(avg)
    print(grades)
    print(middle_grades)


grades_1 = [65, 134, 76, 234, 7, 3, 44]
list.sort(grades_1)

drop_first_last_in_avg(grades_1)
