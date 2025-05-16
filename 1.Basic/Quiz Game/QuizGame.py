# 1. store questions with their options
# 2. user have multiple choices
# 3. store users score
# 4. print the score after user completed the quiz

quiz = [
  ("What is the 1+1?", # question
    ["A. 2", "B. 1", "C. 4", "D. 0"], # options
    "A" # correct option
  )
]

def run_quiz(quiz):
  UserScore = 0
  for question, options, correctOption in quiz:
    print("\n" + question)
    for option in options:
      print(option)
    answer = input('Your answer (A/B/C/D): ').upper()
    if answer == correctOption:
      print('Correct!')
      UserScore += 1
    else:
      print(f"Wrong! The answer was {correctOption}")
  
  print(f"You got {UserScore} out of {len(quiz)} correct!")

run_quiz(quiz)