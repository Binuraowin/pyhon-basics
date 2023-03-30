marks = []
for i in range(5):
    mark = float(input("Enter the mark for student " + str(i+1) + ": "))
    marks.append(mark)


grades = []
for mark in marks:
    if mark > 75:
        grade = "A"
    elif mark >= 65 and mark <= 75:
        grade = "B"
    elif mark >= 55 and mark <= 64:
        grade = "C"
    elif mark >= 45 and mark <= 54:
        grade = "S"
    else:
        grade = "F"
    grades.append(grade)

print(grades)


marks = []
for i in range(10):
    mark = float(input("Enter the mark for student " + str(i+1) + ": "))
    marks.append(mark)

max_mark = max(marks)
min_mark = min(marks)
avg_mark = sum(marks) / len(marks)

print("Maximum mark is:", max_mark)
print("Minimum mark is:", min_mark)
print("Average mark is:", avg_mark)


sum = 0
num = int(input("Enter a number: "))
while num != -999:
    sum += num
    num = int(input("Enter a number: "))
print("The sum of the numbers is:", sum)
