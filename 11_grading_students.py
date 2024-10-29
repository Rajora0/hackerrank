# def gradingStudents(grades):
#     """
#     Adjust student grades based on rounding rules. Grades below 38 remain unchanged,
#     while grades 38 or higher are rounded up to the next multiple of 5 if the difference 
#     between the grade and the next multiple of 5 is less than 3.

#     Args:
#         grades (list of int): A list of integer grades.

#     Returns:
#         list of int: A list of adjusted grades.
#     """
#     # Initialize an empty list to store the adjusted grades
#     adjusted_grades = []

#     # Iterate through each grade in the input list
#     for grade in grades:
#         # Grades below 38 remain unchanged
#         if grade < 38:
#             adjusted_grades.append(grade)
#         else:
#             # If the difference between grade and next multiple of 5 is less than 3, round up
#             if grade % 5 >= 3:
#                 adjusted_grades.append(((grade // 5) + 1) * 5)
#             else:
#                 # Otherwise, keep the original grade
#                 adjusted_grades.append(grade)

#     # Return the list of adjusted grades
#     return adjusted_grades

def gradingStudents(grades):
    """
    Adjust student grades based on rounding rules. Grades below 38 remain unchanged,
    while grades 38 or higher are rounded up to the next multiple of 5 if the difference 
    between the grade and the next multiple of 5 is less than 3.

    Args:
        grades (list of int): A list of integer grades.

    Returns:
        list of int: A list of adjusted grades.
    """
    # Use map to apply the rounding logic to each grade
    return list(map(lambda grade: grade if grade < 38 or grade % 5 < 3 else ((grade // 5) + 1) * 5, grades))


# Example usage
grades = [73, 67, 38, 33]
print(gradingStudents(grades))  # Output: [75, 67, 40, 33]
