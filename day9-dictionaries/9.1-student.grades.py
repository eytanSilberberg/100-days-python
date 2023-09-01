student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    curr_score = student_scores[student]
    if curr_score >= 91 and curr_score <= 100:
        grade = 'Outstanding'
    elif curr_score >= 81 and curr_score <= 90:
        grade = 'Exceeds Expectations'
    elif curr_score >= 71 and curr_score <= 80:
        grade = "Acceptable"
    else:
        grade = 'Fail'
    student_grades[student] = grade


print(student_grades)
