student_heights = input("Write the height of you and your friends in cm separated by a comma!\n").split(",")

total_sum = 0
number_students = 0
for i in student_heights:
    total_sum += int(i)
    number_students += 1
    if i == student_heights[-1]:
        average = total_sum/number_students
        final_average = round(average)
        print(f"The height average is {final_average}!")

