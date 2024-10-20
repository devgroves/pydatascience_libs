import numpy as np
import operator

# Define a structured data type
marksheet = np.dtype([('Grade', 'U10'),('Section', 'U10'),('name', 'U10'), ('total', 'f4')])

# Create a structured array
schoolmarks = np.rec.array([('G1', 'A', 'Nagappan', 55.0), 
                 ('G1', 'A', 'Lavanya', 85.5),
                 ('G2', 'A', 'Krithik', 68.0)], dtype=marksheet)

print(schoolmarks)
print(schoolmarks.name)  # Accessing the 'name' field
print(schoolmarks.Grade == 'G1')   # Accessing the 'age' field

totalMarks = schoolmarks[schoolmarks.Grade == 'G1']

print('filter the marks of G1 grade', totalMarks)

print('Grade g1 total marks:', np.sum(totalMarks.total))

print('Grade g1 average marks:', np.average(totalMarks.total))

# Group by 'grade' and sum 'total'
unique_grades = np.unique(schoolmarks.Grade)
grouped_grade_sumofmarks = {grade: np.sum(schoolmarks[schoolmarks.Grade == grade].total) for grade in unique_grades}
print('total mark in each grade', grouped_grade_sumofmarks)
print(type(grouped_grade_sumofmarks))

grouped_grade_firstmarks = {grade: np.max(schoolmarks[schoolmarks.Grade == grade].total) for grade in unique_grades}
print('first mark in each grade', grouped_grade_firstmarks)


# Find the key with the maximum value
max_key = max(grouped_grade_sumofmarks.items(), key=operator.itemgetter(1))[0]

print("Grade with max total mark:", max_key, grouped_grade_sumofmarks.items())
