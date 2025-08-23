p_students = {"Muzaffar", "Sahil", "Farhan" "Samil"}
J_students = {"Jabbar", "Raj", "Farhan" "Tahir"}
both_course_std = p_students & J_students
all_course_std = p_students | J_students
students_onlyInPython = p_students - J_students
print(f"Taking both {both_course_std}")
print(f"Total students {len(all_course_std)}")
p_students.add("Self")
print(p_students)
p_students.remove("Self")
print(p_students)
p_students.discard("Self")
print(p_students)
total_students = len(all_course_std)
print(f"Total students {total_students}")