#we use the random module to shuffle the questions
import random

questions = [
    {
        "question": "What is the keyword to define a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "question": "Which movie features the quote: 'I'll be back'?",
        "options": ["A) Terminator", "B) Titanic", "C) Avatar", "D) Rocky"],
        "answer": "A"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "answer": "B"
    }
]

def play_quiz():
    score = 0

    #randomly shuffle the questions
    print("Welcome to the Quiz Game!")
    random.shuffle(questions)

    print("Answer the following questions:")
    #loop through each question
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer not in ["A", "B", "C", "D"]:
                print("Invalid input. Please enter A, B, C, or D.")
            else:
                break
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    print(f"\nYour final score: {score}/{len(questions)}")

def main():
    while True:
        play_quiz()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()