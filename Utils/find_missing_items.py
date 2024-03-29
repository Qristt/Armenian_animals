import os 

dir1 = input("Input the first directory path.\n")
list1 =[]
for item in os.listdir(dir1):
  name, ext = os.path.splitext(item)
  list1.append(name)


dir2 = input("Input the second directory path.\n")
list2 =[]
for item in os.listdir(dir2):
  name, ext = os.path.splitext(item)
  list2.append(name)


set_dif = set(list1).symmetric_difference(set(list2))
difference = list(set_dif)

print(difference)