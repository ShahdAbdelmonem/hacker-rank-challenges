from collections import namedtuple
n = int(input())
fields = input().split()

Student = namedtuple('Student', fields)

total_marks = 0

for i in range(n):
    info = input().split()
    student = Student(*info)
    total_marks += int(student.MARKS)

average = total_marks / n
print(f"{average:.2f}")
