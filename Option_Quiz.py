questions = [
    {
        "prompt": "What is the capital of India?",
        "options": ["A. Paris", "B. Delhi", "C. London", "D. None"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest Prime Number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. None"],
        "answer": "B"
    },
    {
        "prompt": "What is the factor of 5?",
        "options": ["A. 120", "B. 80", "C. 150", "D. None"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A,B,C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct, hooray!!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)