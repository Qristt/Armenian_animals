import os

while 1:
	directory = input("\n\nPlease input the path to the working directory\n")
	print("\nYou have named the directory path as: ", directory, "\n")
	while 1:
		answer = input("Are you sure you want use that direcotry? [y]/n\n").lower()
		if answer in ["", "y", "n","yes","no"]:
			break
		else:
			print("Please provide a valid answer!")
	if answer in ["","y","yes"]:
		break


os.chdir(directory)
print(os.getcwd())

files = os.listdir(os.getcwd())
[os.replace(file, file.replace(" ", "_")) for file in files]