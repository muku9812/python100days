# Dictionary Methods in python

students = {1: "Aman",
            2: "Anish",
            3: "Bhuwan",
            4: "Chandan",
            5: "Darshan",
            6: "Elish",
            7: "Ganesh"}
student_new = {8: "Harry",
               9: "Indra",
               10: "Jack",
               11: "Kiran"
               }
students.update(student_new)  # this update function will update the students' dictionary.
print(students)
students.clear()  # this clear function will clear the dictionary
print(students)
student_new.pop(8)  # this pop method will remove the respective data from the dictionary
print(student_new)
student_new.popitem()  # this method will remove last value pair of dictionary
# print(student_new)
del student_new[10]  # this method will delete only one data from the dictionary
print(student_new)


# del students  # the del method will delete the dictionary