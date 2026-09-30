age = int(input("Enter your age "))

if age>=1 and age<=5:
  print("You are child")
elif age>=6 and age<=12:
  print("You are kid")
elif age>=13 and age<=19:
  print("You are teenager")
elif age>=20 and age<=29:
  print("You are young")
elif age>=30 and age<=59:
  print("You are adult")
elif age>=60 and age<=70:
  print("You are senior citizen")
elif age>=71 and age<=80:
  print("You are old")
elif age>=81 and age<=100:
  print("You are very old")
else:
  print("Invalid input")
