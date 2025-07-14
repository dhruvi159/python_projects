#Trivia Game

# ask questions 
# store answers from the user
# randomly pick the questions
# ask the question
# Check answers if they are correct
# keep track of the final score
# Tell the user their score
import random

Questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the largest planet in our Solar System?": "Jupiter",
    "What is the boiling point of water in Celsius?": "100",
    "Who is the author of 'Harry Potter'?": "J.K. Rowling",
    "What is the square root of 16?": "4",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the fastest land animal?": "Cheetah"
}


def python_trivia_game():
    Questions_list = list(Questions.keys())
    score = 0
    total_questions = 5


    random_choice_question = random.sample(Questions_list, total_questions)
    
    for idx, question in enumerate(random_choice_question):
        print(f"{idx}.{question}")
        user_input = input(f"{idx} answer: ").lower().strip()
        correct_answer = Questions[question]
        if user_input == correct_answer.lower():
            print("correct answer")
            score += 1
        else:
            print("Incorrect answer")   
    print(f"Your final score is {score}/{total_questions}")


    

python_trivia_game()

