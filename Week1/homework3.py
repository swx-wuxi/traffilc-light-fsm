student_name = "Alice"
student_age = 23
TOTAL_MARKS = 95


def calculate_average(student_marks):
    return sum(student_marks) / len(student_marks)

class StudentRecord:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = StudentRecord(student_name, student_age)
print(calculate_average([TOTAL_MARKS, 88, 76]))
