#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Please select an option (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    
    if options[answer - 1] == correct_answer:
        print("Correct!:)")
        return True
    else:
        print(f"Oops!Incorrect answer:(")
        print(f"The correct answer is: {correct_answer}")
        return False

def quiz_game():
    questions = [
        {
            "question": "Which of the following is the national river of India?",
            "options": ["Ganga", "Yamuna", "Brahmaputra", "Mahanadi"],
            "answer": "Ganga"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        }
    ]

    score = 0
    total_questions = len(questions)

    for q in questions:
        print("\n")
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print("\nQuiz Completed!")
    print(f"Your final score is: {score}/{total_questions}")

if __name__ == "__main__":
    quiz_game()


# In[ ]:




