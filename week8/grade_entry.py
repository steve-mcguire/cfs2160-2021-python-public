try:
    grades = input("Enter your grades")
    #print(grades)
    grades_list = grades.split(",")
    print(grades_list)
    grades_comprehension = [int(grade) for grade in grades_list]
    print(grades_comprehension)
except ValueError as ve:
    print(ve)
else:
    print("Programme ended")

