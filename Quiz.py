print("Welcome to my Computer Quiz")


Playing = input("Do you Want to play? (yes/no) ").lower()

if Playing == "yes":
    print ("Great ! let's play")

elif Playing == "no":
    print("May be next Time!!!")

else:
    print("Invalid Input, Please enter yes or no ")

score = 0

answer = input(" What is the keyword used to define a function in Python? \n Ans. ").lower()
if answer == "def":
    print("correct")
    score += 1
else :
    print("Incorrect!!")

answer = input("What data type is used to store True or False values in Python? \n Ans.").lower()
if answer == "boolean":
    print("Correct")
    score += 1

else:
    print("Incorrect")

print("Which of the following is NOT a valid variable name in Python?")
print("A. my_var", "B. 2vrnd", "C. Var1", "D. None")

answer = input("Choose the correct option (A,B,C,D): \n Ans.").upper()
if answer =="B":
    print("Correct")
    score += 1

else: 
    print("Incorrect")

print("What is the correct file extension for Python files? ")
print("A. .py", "B. .cpp", "C. .js", "D. None")

answer = input("Choose the correct option (A,B,C,D): \n Ans. ").upper()
if answer == "A":
    print("Correct")
    score += 1
else :
    print("Incorrect")

print("How do you insert a comment in Python code?  ")
print("A. #","B. //","C. !--","D.None")

answer = input("choose the correct option (A,B,C,D): \n Ans.").upper()
if answer == "A":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"You got {score} Questions Correct")

print(f"You scored {(score / 5)* 100}%.")