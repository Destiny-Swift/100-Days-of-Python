students_height = input('Enter the heights of the students:\n').split()

sum_heights = 0
num_students = 0

for i in range(len(students_height)):
    print(i)
    students_height[i] = int(students_height[i])
    sum_heights += int(students_height[i])
    num_students += 1


print(round(sum_heights / num_students))
