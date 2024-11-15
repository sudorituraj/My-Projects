import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10
def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left) + " " + operator + " " + str(right) 
    answer = eval(expression)
    return expression, answer


wrong = 0

input("Press enter to start : ")
print("---------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    
    guess = input("Problem #" + str(i + 1)+": " + expression 
                      + " " + "=" " ")
    if guess == str(answer):
        print("correct")

    else:
        print("Incorrect, The correct answer was",answer) 
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("-------------------")
print("Nice Work! you finished in",total_time, "seconds!")
print("You got",wrong,"problems wrong out of",TOTAL_PROBLEMS)