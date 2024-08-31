from art import logo

print(logo)

def add(f_number, s_number):
  return f_number + s_number

def subtract(f_number, s_number):
  return f_number - s_number

def multiply(f_number, s_number):
  return f_number * s_number

def divide(f_number, s_number):
  return f_number / s_number

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  calculation = True
  first_number = int(input("What's your first number? "))
  
  while calculation:
    for symbols in operations:
      print(symbols)
    operation_symbol = input("Pick an operation: ")
    second_number = int(input("What's your next number? "))
    
    calculate_function = operations[operation_symbol]
    answer = calculate_function(first_number, second_number)
    print(f"{first_number} {operation_symbol} {second_number} = {answer}")
  
    should_continue = input(f"Type 'y' to continue calculating with {answer} or 'n' to stop: ").lower()
  
    if should_continue == 'y':
      first_number = answer
    elif should_continue == 'n':
      calculation = False
      calculator()

calculator()
      