grades = []


def process_grade(grade):
    grades.append(grade)


print("Welcome to the student grade system")


for x in range(5):
    grade = int(input("Please enter a grade"))
    process_grade(grade)


print("Lowest Grade", min(grades))
print("Highest Grade", max(grades))
avg = sum(grades) / len(grades)
if avg < 40:
    print("You have failed")
elif avg < 50:
    print("you have earned a 3rd class grade.")
elif avg < 60:
    print("you have earned a 2.2 class grade.")
elif avg < 70:
    print("you have earned a 2.1 class grade.")
else:
    print("You have earned a first class grade.")