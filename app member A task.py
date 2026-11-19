def grade(mark):
    if not 0 <= mark <= 100:
        return "Invalid mark"
    if mark >= 70:
        return "First"
    if mark >= 60:
        return "2:1"
    if mark >= 50:
        return "2:2"
    if mark >= 40:
        return "Third"
    return "Fail"

students = {}

num_students = int(input("How many students? "))

for i in range(num_students):
    name = input("\nStudent name: ")

    marks = []

    num_modules = int(input("How many modules? "))

    for j in range(num_modules):
        mark = int(input(f"Enter mark for module {j+1}: "))
        marks.append(mark)

    students[name] = marks

print("\nResults")
print("--------")

for name, marks in students.items():
    average = sum(marks) / len(marks)
    print(
        name,
        "Marks:", marks,
        "Average:", round(average, 1),
        "Grade:", grade(average)
    )
