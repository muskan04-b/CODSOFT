def cal(num1, num2, operation):
  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    return num1 / num2
  else:
    print("Invalid operation!")
    return None

def main():

  while True:
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
      break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
      operation = "add"
    elif choice == "2":
      operation = "subtract"
    elif choice == "3":
      operation = "multiply"
    elif choice == "4":
      operation = "divide"
    else:
      print("Invalid choice!")
      continue

    result = cal(num1, num2, operation)
    if result is not None:
      print("* Result:", result,"*")

if __name__ == "__main__":
  main()