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



