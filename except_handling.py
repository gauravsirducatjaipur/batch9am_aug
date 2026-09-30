try:
  f = open("sahil.txt")
  try:
    f.write("Hello user")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")