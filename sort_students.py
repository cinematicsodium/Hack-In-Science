# Part 1
# Write a function named sort_by_MARK that takes an 
# argument [list of students] and returns a copy of 
# it sorted by mark in DESCENDING order. 
# -----------------------------------------------------
# Part 2
# Write a function named sort_by_NAME that takes an 
# argument [list of students] and returns a copy of 
# it sorted by name in ASCENDING order,
# -----------------------------------------------------

def sort_by_mark(my_class):
    my_class.sort(key = lambda x: x[0], reverse=True)
    return my_class

def sort_by_name(my_class):
    my_class.sort(key = lambda x: x[1])
    return my_class

students = [(85, "Susan Maddox"), (6, "Joshua Tran"), (37, "Jeanette Wafer")]

print(sort_by_mark(students))
print(sort_by_name(students))