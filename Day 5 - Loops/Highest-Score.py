student_scores = input("Write the scores of your students!\n").split(",")

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


high_score = 0
for score in student_scores:
    if score> high_score:
        high_score = score

print(f"the highest score is: {high_score}")
