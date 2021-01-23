import os
import platform

global studentlist
studentlist = ["Ram", "Lakshman", "Bharat", "Shatrughn"]

def studentmanagement():

	print("\n++++++ Welcome to Madan Mohan Malaviya University of Technology Student Management System ++++++\n")
	print("[Choice 1:  To show List of Student")
	print("[Choice 2: To Add New Student]")
	print("]Choice 3: Search for a Student]")
	print("[Choice 4: Deleting a Student]\n")

	try:
		x = int(input("Enter a choice: "))
	except ValueError:
		exit("\n This is not a valid Number")
	else:
		print("\n")

	if(x==1):
		print("Student List\n")
		for students in studentlist:
			print("++ {} ++".format(students))

	elif(x==2):
		studentnew = input("Enter New Student: ")
		if(studentnew in studentlist):
			print("\nThis Student {} Already exists In The Table".format(studentnew))
		else:
			studentlist.append(studentnew)
			print("\n++ New Student {} Added Successfully ++\n".format(studentnew))
			for students in studentlist:
				print("++ {} ++".format(students))

	elif(x==3):
		studentsearching = input("Choose Student Name To Search in the database: ")
		if(studentsearching in studentlist):
			print("\n++ There is a Record Found of this Student {} ++".format(studentsearching))
		else:
			print("\n++ There is No Record Found Of this Student {} ++".format(studentsearching))

	elif(x==4):
		studentdelete = input("Choose a Student Name To Delete: ")
		if(studentdelete in studentlist):
			studentlist.remove(studentdelete)
			for students in studentlist:
				print("++ {} ++".format(students))
		else:
			print("\n++ There is No Record Found of This Student {} ++".format(studentdelete))

	elif(x < 1 or x > 4):
		print("Please Enter Valid Choice")

studentmanagement()

def continueAgain():
	runningagain = input("\nWant to continue yes/no?: ")
	if(runningagain.lower() == 'yes'):
		if(platform.system() == "Windows"):
			print(os.system('cls'))
		else:
			print(os.system('clear'))
		studentmanagement()
		continueAgain()
	else:
		quit()

continueAgain()
