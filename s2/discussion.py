#arithmetic operations

num1 = 25
num2 = 50

sum = num1 + num2

print(f"The total sum of {num1} and {num2} is {sum}")

#addition
#+

#subtraction
#-

#multiply
#*

#divide
#/

#modulo
#remainder
#%

#pemmdas -> () * / + -
pemmdas = (2 + 2) + 3 * 2
print(pemmdas)

#comparison operator
#boolean datatype

#== equal
num1 = 10
num2 = 11

letter1 = "s"
letter2 = "a"

print(num1 == num2)
print(letter1 == letter2)

#age = int(input("Enter your age: "))
#age = input("Enter your age: ")

#not equal
#!=

print(f"true or false: {letter1} is not equal to {letter2}: answer: {letter1 != letter2}")

#< or <=

num3 = 900
num4 = 900

print("------------------")
print(num3 < num4)
print(num3 <= num4)

#> or >=

print("---------")
print(num3 > num4)
print(num3 >= num4)

#if else

legal_age = 18

if legal_age >= 18:
    print("You are now 18 and above")
else:
    print("You are not yet 18 years old")

#grade = int(input("Enter your grade: "))

# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# else:
#     print("You Fail")

# if grade >= 70 and grade <= 79:
#     print("C")
# elif grade >= 80 and grade <= 89:
#     print("B")
# elif grade >= 90 and grade <= 100:
#     print("A")
# else:
#     print("You Fail")

#logical operator
#and -> statement should both be true

# or -> statement should be atleast 1 is true
data1 = 2
data2 = 2
data3 = 5

if data1 == 1 or data2 == 1 or data3 == 1:
    print(f"Your data is 1")
else:
    print("No data is 1")



# not -> reverse value 


is_student = False

if not is_student:
    print("A student")
else:
    print("Not a student")
