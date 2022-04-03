def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]+ marks[3])/500 )*100
    return p

marks1 = [93, 72, 86, 69, 75]
percentage1 = percent(marks1)

marks2 = [45, 59, 48, 61, 41]
percentage2 = percent(marks2)

marks3 = [75, 89, 68, 31, 61]
percentage3 = percent(marks3)
print(percentage1, percentage2, percentage3)