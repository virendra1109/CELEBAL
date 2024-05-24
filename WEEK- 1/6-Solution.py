# Read number of students
n = int(input())

# Initialize an empty dictionary to store student records
student_marks = {}

# Read the next n lines for student names and their respective marks
for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

# Read the name of the student to query
query_name = input()

# Retrieve the marks for the query_name
marks = student_marks[query_name]

# Calculate the average of the marks
average = sum(marks) / len(marks)

# Print the average rounded to 2 decimal places
print(f"{average:.2f}")
