grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
grades1 = sum(grades[0])/len(grades[0])
grades2 = sum(grades[1])/len(grades[1])
grades3 = sum(grades[2])/len(grades[2])
grades4 = sum(grades[3])/len(grades[3])
grades5 = sum(grades[4])/len(grades[4])
grades = [grades1, grades2, grades3, grades4, grades5]
average_rating = dict(zip(students, grades))
print(average_rating)