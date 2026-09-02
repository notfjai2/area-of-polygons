def square():
  try:
    a = input("Side: ")
    return a ** 2
  except valueError:
    print("Please enter a valid number.")
    a = input("Side: ")