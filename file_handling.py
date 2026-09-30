# # f1 = open("demo.txt")
# # data = f1.read()
# # print(data)

# # f1 = open("demo.txt")
# # print(f1.read())
# # f1.close()

# # with open("mymodule.py") as f2:
#   # print(f2.read(5))
#   # print(f2.readline())
#   # print(f2.readlines())


# # with open("mymodule.py") as f2:
# #   data = f2.readlines()
# #   for x in data:
# #     print(x)

# # with open("demo1.txt", "w") as f3:
# #   f3.write("\nNow the file has more content!")
# #   print("Data has been written successfully")


# # with open("demo.txt", "a") as f3:
# #   f3.write("\nNow the file has more content!")
# #   print("Data has been modified successfully")


# # with open("demo3.txt", "a") as f3:
# #   f3.write("\nNow the file has more content!")
# #   print("Data has been modified successfully")


# with open("demo.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #open and read the file after the overwriting:
# with open("demo.txt") as f:
#   print(f.read())




# read
# write
# append

# with open("demo.txt", "r") as f1:
#   data = f1.read()
#   print(data)


# with open("demo.txt", "w") as f1:
#   f1.write("welcome in write mode...")

# with open("demo.txt", "r") as f1:
#   print(f1.read())




# with open("demo.txt", "a") as f1:
#   f1.write("now the file has more content...")

# with open("demo.txt", "r") as f1:
#   print(f1.read())


import os

if os.path.exists("demo1.txt"):
  os.remove("demo1.txt")
  print("The file has been deleted successfully")
else:
  print("The file does not exist")