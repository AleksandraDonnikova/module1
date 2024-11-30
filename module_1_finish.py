grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
students = sorted(students)
jornual = {}
for student, s_grade in zip(students, grades):
#print(student, grades)
    result = sum(s_grade)/len(s_grade)
    jornual[student] = result
print(jornual)



