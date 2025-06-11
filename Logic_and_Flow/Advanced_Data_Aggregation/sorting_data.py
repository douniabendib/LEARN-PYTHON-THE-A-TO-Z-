"""
Create a function named analyze_grades that takes a dictionary 
of student grades as an argument. The dictionary keys are student names, 
and the values are their corresponding grades. The function should 
perform the following operations:

Calculate the average grade of all students.
Find the highest and lowest grades.
Identify the student(s) with the highest and lowest grades.
Return a dictionary containing the following information:
'average': The average grade (rounded to 2 decimal places)
'highest': The highest grade
'lowest': The lowest grade
'top_student': The name of the student with the highest grade
'bottom_student': The name of the student with the lowest grade
"""
def analyze_grades(grades):
    somme = 0
    for value in grades.values():
        somme += value
    average_grade = somme/len(grades)
    highest_grade = max(grades.values())
    lowest_grade = min(grades.values())
    top_student = max(grades, key=grades.get)
    bottom_student = min(grades, key=grades.get)
    return {
       'average' : average_grade,
       'highest' : highest_grade,
       'lowest': lowest_grade,
       'top_student': top_student,
       'bottom_student': bottom_student
    }   


student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)
