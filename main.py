# ==============================
# Student Course Tracker
# Starter Template
# ==============================

# Starter data (DO NOT MODIFY)
students = [
    ("Alice", 20),
    ("Bob", 22),
    ("Charlie", 21)
]

courses = ["Python", "JavaScript", "Python", "Databases"]

student_data = {
    "Alice": {"courses": ["Python", "Databases"], "grades": [85, 90]},
    "Bob": {"courses": ["Python", "JavaScript"], "grades": [78, 82]},
    "Charlie": {"courses": ["JavaScript"], "grades": [88]}
}

# ------------------------------
# Task 1: Remove Duplicate Courses
# ------------------------------
# TODO:
# - Convert the courses list into a set
# - Print the unique courses

unique_courses = set(courses)
unique_courses_list = list(unique_courses)
print(f"unique courses: {', '.join(unique_courses_list)}")


# ------------------------------
# Task 2: Display Student Info
# ------------------------------
# TODO:
# - Loop through the students list
# - For each student, print:
#   Name, age, and enrolled courses

for name, age in students:
    enrolled_courses = student_data[name]["courses"]
    enrolled_courses_string = ', '.join(enrolled_courses)
    print(f"{name} is {age} years old and enrolled in {enrolled_courses_string}")

# ------------------------------
# Task 3: Add Course for Bob
# ------------------------------
# TODO:
# - Add "Databases" to Bob's course list
#   ONLY if he is not already enrolled
# - Print Bob's updated course list

if "Databases" not in student_data["Bob"]['courses']:
    student_data["Bob"]['courses'].append('Databases')

print(f"Bob is enrolled in {', '.join(student_data["Bob"]['courses'])}")

# ------------------------------
# Task 4: Calculate Average Grades
# ------------------------------
# TODO:
# - Loop through student_data
# - Calculate and print each student's average grade

highest_avg = 0
highest_avg_student = ''

for student, data in student_data.items():
    grades = data["grades"]

    avg = sum(grades) / len(grades)
    
    print(f"{student}'s average grade is {avg:.1f}")

    data["average_grade"] = avg

    if avg > highest_avg:
        highest_avg = avg
        highest_avg_student = student

print(f"{highest_avg_student} has the highest average at {highest_avg}")

# ------------------------------
# Task 5: Find Students in a Course
# ------------------------------
# TODO:
# - Ask the user to enter a course name
# - Print all students enrolled in that course

chosen_course = input('give me a course name').lower()

students = []

for student, data in student_data.items():
    if chosen_course.capitalize() in data["courses"]:
        students.append(student)

print(f"{' and '.join(students)} are enrolled in {chosen_course}")


# ------------------------------
# Bonus (Optional)
# ------------------------------
# TODO:
# - Store each student's average grade in the dictionary
# - Print the student with the highest average grade
