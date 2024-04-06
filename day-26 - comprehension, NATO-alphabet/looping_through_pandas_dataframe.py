import pandas as pd

students_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98],
}

# # Looping through dictionaries
# for (key, value) in students_dict.items():
#     print(key)
#     print(value)

# Looping though DataFrames
students_data = pd.DataFrame(students_dict)
print(students_data)

# # Conventional method
# for (key, value) in students_data.items():
#     print(value)

# Pandas inbuilt loop
for (index, row) in students_data.iterrows():
    if row.student == 'Angela':
        print(row.score)
