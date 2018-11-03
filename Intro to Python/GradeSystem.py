import os

def clear():
	os.system('cls')

subjects = ["English", "Maths", "History", "Science"]		

class Student:
	'''This is a student class, it stores all the details of a perticular student'''
	def __init__(self, name, roll_number, marks):
		'''
			accepted value of name = 'str'
			accepted value of roll_number = 'int'
			accepted value of marks = 'list['int']'
		'''
		self.name = name
		self.roll_number = roll_number
		self.marks = {}
		average = 0
		for i in range(4):
			self.marks[subjects[i]] = marks[i]
			average += marks[i]

		average /= len(marks)
		self.average = average

	def print_details(self):
		print("{} | {}".format(self.name, self.roll_number))

	def get_details(self):
		return (self.name + " | " + str(self.roll_number))

	def print_marks(self):
		for subject in self.marks:
			print("{}:{}  ".format(subject, self.marks[subject]), end='')
		print()
		print("Average Marks: {}".format(self.average))


#will hold roll numbers of students who scored maximum marks in the subject
max_marks = {"English":"n/a", "Maths":"n/a", "History":"n/a", "Science":"n/a"}

#will store all the details in the form of {roll_number:Student}
#where roll_number is the roll number of the student & Student is an instance of class Student
stu_list = {}	#student list

#a list to store marks
marks = []	#list of marks in English, Maths, History, Science in same order

no_of_students = int(input("Enter the number of students: ")) 

for student in range(no_of_students):
	name = input("Enter Name of Student {}: ".format(student + 1))
	roll_number = int(input("Enter Roll Number of Student {}: ".format(student + 1)))

	for subject in subjects:
		marks.append(int(input("Enter Marks for {}: ".format(subject))))
	print()

	kido = Student(name, roll_number, marks)
	stu_list[kido.roll_number] = kido
	marks.clear()

	if (student == 0):
		max_marks["English"] = kido.roll_number
		max_marks["Maths"] = kido.roll_number
		max_marks["History"] = kido.roll_number
		max_marks["Science"] = kido.roll_number
	else:
		for max_subject in max_marks:
			#kido1 has the maximum marks in max_subject
			kido1 = stu_list[max_marks[max_subject]]
			if kido.marks[max_subject] > kido1.marks[max_subject]:
				max_marks[max_subject] = kido.roll_number


clear()
print("Student List:")
for student in stu_list:
	stu_list[student].print_details()
	stu_list[student].print_marks()
	print()

print()

print("Top Scorers: ")
for max_subject in max_marks:
	kido = stu_list[max_marks[max_subject]]
	print("{}: {}".format(max_subject, kido.get_details()))
