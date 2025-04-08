n = int(input())
students  = []
for _ in range(n):
    name = input()
    score  = float(input())
    students.append([name, score])
grades = sorted(set([student[1] for student in students]))
second_lowest = grades[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest]
second_lowest_students.sort()
for student in second_lowest_students:
    print(student)


