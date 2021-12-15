student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key,values in student_scores.items():
  if 91 <= values <=100:
    student_grades[key] = "Outstanding"
  elif 81 <= values <=90:
    student_grades[key] = "Exceeds Expectation"
  elif 71 <= values <=80:
    student_grades[key] = "Acceptable"
  elif values <=70:
    student_grades[key] = "Fail"

  
print(student_grades)
