import random
import time

print("Welcome to our kahoots!")
# add a score 
# add a score variable to store what our current score is
score = 0
# take a users input to get their name
name = input("What is your name?").strip()

print("Hello", name, "Let's start our game!")
# start with simple dummy question to test
# (one = is assigning to a variable)
# answer = input("What language is this quiz written in?").strip().lower()

# We need to have a way to say "If you got it right, then output correct, otherwise tell them wrong answer"
# (two == is checking if a value is equivalent to)
# if answer == "python":
#     print("Correct!")
#     # update score if answer is correct
#     score

# Create a list of four letters that can be associated with the correct answer i.e. A, B, C, D
letters = ["A", "B", "C", "D"]
# Lets create a dictionary object with all of our questions stored inside of it that we can access randomly and however many we want

questions = {
    # question1 : answer1,
    "What language is this quiz written in?":{
        # give list of option to choose from
        "options":["Python", "JS", "C++", "Ruby"],
        # from those options, which one is correct?
        "answer":"A"
    },
    "What symbol is used to write a comment in python":{
        "options": ["/", "#", "&", "~"],
        "answer": "B"
    },
    "What function is used to display text in our terminal?":{
        "options":["display", "touch", "write", "print"],
        "answer":"D"
    }
}



# randomize the questions into a list
question_list = list(questions.keys())
# print(question_list)
random.shuffle(question_list)
# print(question_list)
# print(questions["What function is used to display text in our terminal?"])
# print(questions.keys())
print("Your score is:", score)
# print(questions.values())
# print(questions)

# come up with a way to loop over our questions
for question in question_list:
    print("\n" + question)
    # we need to define and then print each of our options
    options = questions[question]["options"]

    for letter, option in enumerate(options):
        print(letters[letter] + ".", option)

    start_time = time.time()
    # print(start_time)

    answer = input("Your answer:").strip().upper()

    end_time = time.time()
    # print(end_time)

    time_taken = end_time - start_time
    # print(time_taken)
    print("You took", round(time_taken,2), "seconds")

    if time_taken > 10:
        print("Too slow! No points this round!")
        print("Your score this round is:", score)
    elif answer == questions[question]["answer"]:
        print("\nCorrect! Score +100")
        # update score if answer is correct
        score = score + 1
    else:
        print("Wrong answer")

print("\nFinal Score:", score)
# Lets see what our percentage correct was!
percentage = round((score / len(questions))*100)
print("\nYou got", percentage, "% correct!")
# print(questions["What function is used to display text in our terminal?"])
# print(questions["What language is this quiz written in?"])
# print(questions["What symbol is used to write a comment in python"])