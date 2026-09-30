import mymath

num = int(input("Enter the first number "))

choice = int(input("Enter your choice between 1 to 3\nPress\n1. for square\n2. for cube\n3. for square root\n"))

if choice ==1:
  print(mymath.square(num))
elif choice ==2:
  print(mymath.cube(num))
else:
  print(mymath.square_root(num))


# result = mymath.square(num)
# print(result)
# print(mymath.square(num))

# import numpy as np

# print(np.random.randint(1, 100, 10))

