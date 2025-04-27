s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()
print(type(harry))

for value in info:
  print(value)

def square(n):
  # docstring statement is just below the fuction definiton
  '''Takes in a number n, returns then square of n'''
  print(n**2)

square(384979)
print(square.__doc__)
# by changing the docstring of the function we can change the function docstring
# docstring is not a comment
# Recurison 
# to call the function inside the function

# factorial(7)=7*6*5*4*3*2*1
def factorial(n):
  if n == 0 or n == 1:  # Base case: factorial of 0 and 1 is 1
      return 1
  else:
      return n * factorial(n - 1)  # Recursive case

# Loop to print the factorial of numbers from 0 to 5
for i in range(6):
  print(f"Factorial of {i} is {factorial(i)}")

def febo(n):
  if (n == 0):

      return 0
  else:
      return n + febo(n-1)


for i in range(6):
  print(f"Factorial of {i} is {factorial(i)}")
  # set methods
  # union() and udates()
  s1={1,2,3,4,5}
  s2={3,4,5,6,7}
  print(s1.union(s2))
  s1.update(s2) # it will update the s1 with the values of s2
  print(s1,s2)
  # intersection and intersection_updates()
  s3 = s1.symmetric_difference(s2)#it will print the values which are not common in the both sets
  print(s3)
  s1.symmetric_difference_update(s2)# it will update the s1 with the value which are not common in the both sets 
  print(s1)
  # difference and difference_update()
  s4 = s1.difference(s2)
  print(s4)#it will print the values which are present in s1 but not in s2
  s1.difference_update(s2)
  print(s1)
  s1.difference_update(s2)
  print(s1)
  print(s1.isdisjoint(s4))
  print(s1.isdisjoint(s4))
  print(s1.issuperset(s2))
  print(s2.issubset(s1))
  s1.add(9)#to add element in the ser
  s1.remove(9)#if the element is not present in the set then it will raise the error
  s1.discard(9)#it will not raise any error in the execution if element ids not present in the set
  fuck={6,4,6,7}
  item=fuck.pop()#it will pop the random element from the set
  print(item)
  del fuck#it will delete the entire set
  print(fuck)#it will raise the error as the set is deleted
# dictionaries
dic ={
  "harsh":"ashique" ,
  "aditya":"A.T ka ashique" ,
  "age":"18" ,
}
print(dic["aditya"])
print(dic["age"])
print(dic.get("age"))# it will not throw error if the key is not present in the dictionary
# Consider this snippet from ./programs.py
# # program to check the eligibility to vote
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
# methods of dictionary 
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
# ep1.update(ep2)
# ep1.clear() 
# ep1.pop(222)
ep1.popitem()
del ep1[122]
print(ep1)


# program to check the eligibility to vote
x="check for eligiblity"
print(x.center(80))
age=input("enter the age")
age=int(age)
if(age<18):
  print("you are not eligible for vote")
else:
  print("you are eligible for vote")


# Program 1: Grade Calculator
def grade_calculator():
    print("\n=== GRADE CALCULATOR ===")
    score = float(input("Enter your score (0-100): "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Your grade is: {grade}")

# Program 2: BMI Calculator
def bmi_calculator():
    print("\n=== BMI CALCULATOR ===")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

# Program 3: Number Analyzer
def number_analyzer():
    print("\n=== NUMBER ANALYZER ===")
    num = int(input("Enter an integer: "))

    if num == 0:
        print("You entered zero.")
    else:
        # Check if positive or negative
        if num > 0:
            print("The number is positive.")
        else:
            print("The number is negative.")

        # Check if odd or even
        if num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

        # Check if prime
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print("The number is prime.")
            else:
                print("The number is not prime.")

# Program 4: Tax Calculator
def tax_calculator():
    print("\n=== TAX CALCULATOR ===")
    income = float(input("Enter your annual income: $"))

    if income <= 10000:
        tax_rate = 0
    elif income <= 40000:
        tax_rate = 0.1
    elif income <= 80000:
        tax_rate = 0.2
    else:
        tax_rate = 0.3

    tax = income * tax_rate
    net_income = income - tax

    print(f"Tax rate: {tax_rate*100:.1f}%")
    print(f"Tax amount: ${tax:.2f}")
    print(f"Net income: ${net_income:.2f}")

# Program 5: Triangle Type Classifier
def triangle_classifier():
    print("\n=== TRIANGLE CLASSIFIER ===")
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    # Check if it's a valid triangle
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("This is an equilateral triangle.")
        elif a == b or b == c or a == c:
            print("This is an isosceles triangle.")
        else:
            print("This is a scalene triangle.")

        # Check if it's a right triangle
        sides = [a, b, c]
        sides.sort()
        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 0.001:  # Account for floating point imprecision
            print("This is also a right triangle.")
    else:
        print("These sides cannot form a triangle.")

# Program 6: Season Determiner
def season_determiner():
    print("\n=== SEASON DETERMINER ===")
    month = input("Enter month (e.g., January): ").lower()
    day = int(input("Enter day (1-31): "))

    if month in ["december", "january", "february"]:
        season = "Winter"
    elif month in ["march", "april", "may"]:
        season = "Spring"
    elif month in ["june", "july", "august"]:
        season = "Summer"
    elif month in ["september", "october", "november"]:
        season = "Fall"
    else:
        print("Invalid month entered.")
        return

    # Special cases for season boundaries
    if month == "march" and day < 20:
        season = "Winter"
    elif month == "june" and day < 21:
        season = "Spring"
    elif month == "september" and day < 22:
        season = "Summer"
    elif month == "december" and day < 21:
        season = "Fall"

    print(f"The season is: {season}")

# Main program
def main():
    while True:
        print("\n===== INTERMEDIATE PROGRAMMING PRACTICE =====")
        print("1. Grade Calculator")
        print("2. BMI Calculator")
        print("3. Number Analyzer")
        print("4. Tax Calculator")
        print("5. Triangle Classifier")
        print("6. Season Determiner")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            grade_calculator()
        elif choice == '2':
            bmi_calculator()
        elif choice == '3':
            number_analyzer()
        elif choice == '4':
            tax_calculator()
        elif choice == '5':
            triangle_classifier()
        elif choice == '6':
            season_determiner()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# for loop conditiomn statments 
for i in range(12):
  if(i==10):
    print("skip the iteration")
    continue
  print(i)
  # while loopm syntax  
  i=0
  while(i<4):
    print(i)
    i = i + 1

  a="done with the loop"
  print(a.center(69))
    # break statements 
    
    
i=0
for i in range(12):
      print("5X",i+1,"=",5*(i+1))
      if(i == 10):
        print("Loop ends here")
        break

# Program to print multiples of 12 from 0 to 12
for i in range(13):
  if i == 10:
    print("Skipping iteration 10")
    continue
  print("12 x", i, "=", 12 * i)

print("\nDone with the loop")
# do while loop with condition statement
i=0
while True:
  print(i)
  i = i + 1
  if(i%10==0):
    break
# /functiond
# def greet(name):
def calu(a,b): 
  avg=(a+b)/2
  print(avg)
a=52
b=112
if(a>b):
  print("first number is greater")
elif(b==a):
  print("both are equal")
else:
  print("second number is greater")
# avg=(a+b)/2
# print(avg)
calu(a,b)

# pass statement is used to pass the excecution to the next statment
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)

# use of f strings
letter = "hey my name is{} and i an from {}"
country = "russia"
name = "Harsh"
print(f"hey my name is {name} and i am from{country}")
# use of docstrings
def square(n):
    '''Takes in a number n, returns then square of n'''
    print(n**2)

square(5)

print(square.__doc__)

# recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 and 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Loop to print the factorial of numbers from 0 to 5
for i in range(6):
    print(f"Factorial of {i} is {factorial(i)}")