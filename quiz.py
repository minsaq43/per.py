# python quiz game

questions = ("What is the capital of France?",
              "What is the largest planet in our solar system?", 
              "What is the chemical symbol for gold?",
              "How many continents are there on Earth?"
              , "How many bones are in the human body?"
              , "What is the smallest continents of the earth?")
options = (("A. Paris", "B. London", "C. Rome","D. New York")
           , ("A. Earth", "B. Jupiter", "C. Mars","D. Venus")
           , ("A. Au", "B. Ag", "C. Fe", "D. Zn")
           , ("A. 7", "B. 206", "C. 106", "D. 50")
           , ("A. 206", "B. 207", "C. 208", "D. 209")
           ,("A. Asia", "B. Africa", "C. Europe" , "D. Australia"))
answers = ("A", "B", "A", "A", "A", "D")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("Welcome to the quiz!")
    print(question)
    for option in options[questions_num]:
        print(option)
    guess = input("Enter your answer (A, B, C, or D): ")
    guesses.append(guess)
    if guess == answers[questions_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[questions_num]}")
    questions_num += 1
print("Quiz completed! 🎉")

print("Answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is: {score:.2f}%")