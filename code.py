import json
import random

# examples for making and packing questions
print("Welcome to my home. I believe " +
      "that I can guess what you are thinking.")

# list to store question tags to access correct answers
tagList = [0]*20
answerList = [] # list to store possible answers pulled from doc
alreadyAsked = [] # list of question IDs to prevent asking same q
qIndex = 0 # index of currently accessed question

# reads file.txt and stores question data in a dict
with open('file.txt', 'r') as fileQ:
    questions = json.load(fileQ)
print(questions)
# reads answer.txt and stores answer data in a dict
with open('answer.txt', 'r') as fileA:
    answers = json.load(fileA)
print(answers)
# sets up a new dict with same parameters to have an editable
# dict with the answers
possibleAnswers = answers
# iterative values
count = 0
a = 1

########################################################

# main while loop of program that asks questions
while count < 20:
    if count == 5:
        # generates a random index for a question to be accessed
        for x in range(1):
            qIndex = random.randint(1, len(questions))
        # ensures that the random index hasn't already been asked
        # if it has, re-generate a number
        while qIndex in alreadyAsked:
            for x in range(1):
                qIndex = random.randint(1, len(questions))
        alreadyAsked.append(qIndex) # add index to already asked list
    elif count

    questionCurrent = (questions["question" + str(qIndex)])
    print(questionCurrent["question"])
    cond = 1 # variable to ensure correct input
    while cond != 0:
        answer = input("")
        if answer == "yes":
            # adds yesTag associated with question to list
            tagList[count] = questionCurrent["yTag"]
            cond = 0
        elif answer == "no":
            # adds noTag associated with question to list
            tagList[count] = questionCurrent["nTag"]
            cond = 0
        else:
            print("please enter 'yes' or 'no' ")
    count += 1

# randomly selects an answer in array to guess
for y in range(1):
    index = random.randint(0, len(answers))
guess = (answers["ID" + str(0)])
print("Was it " + guess["name"])

# checks to see if guess was correct, and ensures correct input
cond = 1
while cond != 0:
    correct = input("")
    if correct == "yes":
        print("I knew it! Thanks for playing.")
        cond = 0
    elif correct == "no":
        cond = 0
    else:
        print("please enter 'yes' or 'no' ")

# adds answer to array if guess was wrong
if cond == 0:
    # gets animal from user
    print("What was the animal?")
    rightAnimal = input("")
    # creates a dict with the string from user and the existing tagList
    animal = {"name" : rightAnimal, "tag" : tagList}
    animalID = "ID" + str(len(answers))
    answerToWrite = {animalID : animal}
    # appends new answer to the existing file
    with open('answer.txt', 'a') as fileA:
        fileA.write(json.dumps(answerToWrite))
    print("Darn! You got me. Thanks for playing!")