#Question 1
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}! Welcome to the Python programming class.")

greet("Loyd", "Ohene")
greet("Steph", "Oduro")
greet("Daphne", "Agyeman")


#Question 2
def multiply (lenght, width):
    return lenght * width
area1 = multiply(5,10)
area2 = multiply(7,12)
area3 = multiply(4,8)
print(area1)
print(area2)
print(area3)

#Question3
def make_pizza(size, toppings):
    print(f"making a {size} pizza with {toppings}")

make_pizza("size:small", "toppings:beef")

#Question 4
def print_numbers(n):
        print(f"numbers 1 to {n}: ")
        for numbers in range(2, 1 + n, 2):
            print(numbers)
print_numbers(17)
print_numbers(15)

#Question 5
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return(True)
    else:
       return(False)

years = (2020,1900,2000 )
for year in years:
 if leap_year(year):
     print(f"{year} is a leap year")
 else:
     print(f"{year} not a leap year")

#Question 6
 def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"

print(calculator(17, 2, "multiply"))
print(calculator(15, 7, "divide"))
print(calculator(45, 3, "add"))
print(calculator(13, 9, "subtract"))
print(calculator(13, 0, "divide"))