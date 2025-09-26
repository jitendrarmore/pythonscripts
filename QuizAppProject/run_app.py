# run_app.py

from Questions import questions

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct!")

run_quiz(questions)