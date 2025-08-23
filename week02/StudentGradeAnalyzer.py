def add_student(student_list, name, grade1, grade2, grade3):
    """Adds a new student record to the list."""
    student_record = (name, grade1, grade2, grade3)
    student_list.append(student_record)


def calculate_average(student):
    """Calculates the average grade for a student."""
    name, grade1, grade2, grade3 = student  # Tuple unpacking
    return (grade1 + grade2 + grade3) / 3


def calculate_class_stats(student_list):
    """Calculates class statistics."""
    total_grades = 0
    total_students = len(student_list)
    highest_grade = float('-inf')  # Initialize to negative infinity
    lowest_grade = float('inf')    # Initialize to positive infinity

    for student in student_list:
        name, grade1, grade2, grade3 = student  # Unpacking
        avg_grade = calculate_average(student)
        total_grades += avg_grade
        highest_grade = max(highest_grade, avg_grade)
        lowest_grade = min(lowest_grade, avg_grade)

    class_average = total_grades / total_students if total_students > 0 else 0  # Handle empty class
    return class_average, highest_grade, lowest_grade


# Example Usage:
student_records = []

add_student(student_records, "Alice", 85, 90, 78)
add_student(student_records, "Bob", 76, 88, 92)
add_student(student_records, "Charlie", 92, 80, 85)

class_stats = calculate_class_stats(student_records)

print("Class Average:", class_stats[0])
print("Highest Grade:", class_stats[1])
print("Lowest Grade:", class_stats[2])
