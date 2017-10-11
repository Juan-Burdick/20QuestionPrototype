import json
import random

# examples for making and packing questions
print("20q project")

# array to store question tags
tagList = [0]*20
answerList = []
alreadyAsked = []
qIndex = 0
# reads file.txt and stores question dict @param data
with open('file.txt', 'r') as fileQ:
    questions = json.load(fileQ)
print(questions)
# reads answer.txt and stores answers dict
with open('answer.txt', 'r') as fileA:
    answers = json.load(fileA)
print(answers)
possibleAnswers = answers



count = 0
a = 1



# main while loop of program that asks questions
while count < 5:
    for x in range(1):
        qIndex = random.randint(1, len(questions))
    while qIndex in alreadyAsked:
        for x in range(1):
            qIndex = random.randint(1, len(questions))
    alreadyAsked.append(qIndex)
    questionCurrent = (questions["question" + str(qIndex)])
    print(questionCurrent["question"])
    cond = 1
    while cond != 0:
        answer = input("")
        if answer == "yes":
            tagList[count] = questionCurrent["yTag"]
            cond = 0
        elif answer == "no":
            tagList[count] = questionCurrent["nTag"]
            cond = 0
        else:
            print("please enter 'yes' or 'no' ")
    count += 1

for y in range(1):
    index = random.randint(0, len(answers))
guess = (answers["ID" + str(0)])
print("Was it " + guess["name"])
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
# makes questions with tagList and animal
    # needs if statement to decide if answer
    # exists or needs creation