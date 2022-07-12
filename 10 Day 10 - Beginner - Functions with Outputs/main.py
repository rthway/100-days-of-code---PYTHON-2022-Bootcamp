def my_function():
    do this
    then do this
    finnaly do this 
my_function()

# Function with input 
def my_function(something):
    do this with something
    then do this
    finally do this 
my_function()

# Function with output
def my_function():
    result = 3*2
    return result
my_function()

# Q.1 - WAP to display capitalize each word with 2 values
def format_name(f_name,l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"
print(format_name("AnGelA", "YU"))


# Multiple return Value
def format_name(f_name,l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"
print(format_name(input("What is your first name? "), input("What is your last name?")))

# Days in month using function with output
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
    return "Invalid month entered."
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]



#Do NOT change any of the code below 👇
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# Project_10_Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()

