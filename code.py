import json
import random

tagList = [0]*20  # list to store question tags to access correct answers
answerList = []  # list to store possible answers pulled from doc
alreadyAsked = []  # list of question IDs to prevent asking same q
qIndex = 0  # index of currently accessed question
iterator = 0  # iterative value
allTags = []  # allTags, loaded to check most common tag in answers
tagRarity = []  # sibling to allTags, contains rarity of each tag
tagIterator = 0  # iterator for filling allTags

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

# populate allTag list
while tagIterator < len(questions):
    curQ = questions["question" + str(tagIterator + 1)]
    allTags.append(curQ["yTag"])
    tagRarity.append(0)
    allTags.append(curQ["nTag"])
    tagRarity.append(0)
    tagIterator += 1
print(allTags)
tagIterator = 0

########################################################

print("Welcome to my home. I believe " +
      "that I can guess what you are thinking.")
# main while loop of program that asks questions
while iterator < 20:
    # randomly generate the first 5 questions to get a baseline
    if iterator < 5:
        # generates a random index for a question to be accessed
        for x in range(1):
            qIndex = random.randint(1, len(questions))
        # ensures that the random index hasn't already been asked
        # if it has, re-generate a number
        while qIndex in alreadyAsked:
            for x in range(1):
                qIndex = random.randint(1, len(questions))
        alreadyAsked.append(qIndex)  # add index to already asked list
    # intelligently select the rest
    elif 5 <= iterator < 20:
        # generate the rarity of all tags
        while tagIterator < len(answers):
            ans = answers["ID" + str(tagIterator)]
            subTagIterator = 0
            while subTagIterator < len(allTags):
                # only increment rarity if the tag appears
                if allTags[subTagIterator] in ans["tag"]:
                    tagRarity[subTagIterator] += 1
                subTagIterator += 1  # move subIterator
            tagIterator += 1  # move iterator

        tagIterator = 0  # reset iterator so it can be reused
        indexOfMostCommon = 0  # used to keep track of the most common tag
        # find the index of the most common tag
        # so we can access it from the allTags list
        while tagIterator < len(tagRarity):
            if tagRarity[tagIterator] > indexOfMostCommon:
                indexOfMostCommon = tagRarity[tagIterator]
            tagIterator += 1  # move iterator

        tagIterator = 1  # reset iterator so it can be reused
        # get the question associated with the most common tag
        while tagIterator < (len(questions) + 1):
            curQ = questions["question" + str(tagIterator)]
            if allTags[indexOfMostCommon] == curQ["yTag"]:
                qIndex = tagIterator
            elif allTags[indexOfMostCommon] == curQ["nTag"]:
                qIndex = tagIterator
            tagIterator += 1  # move iterator

    questionCurrent = (questions["question" + str(qIndex)])
    print(questionCurrent["question"])
    cond = 1  # variable to ensure correct input
    while cond != 0:
        answer = input("")
        answer.lower()
        if answer == "yes":
            # adds yesTag associated with question to list
            tagList[iterator] = questionCurrent["yTag"]
            cond = 0
        elif answer == "no":
            # adds noTag associated with question to list
            tagList[iterator] = questionCurrent["nTag"]
            cond = 0
        else:
            print("please enter 'yes' or 'no' ")
    iterator += 1

# randomly selects an answer in array to guess
for y in range(1):
    index = random.randint(0, len(answers))
guess = (answers["ID" + str(0)])
print("Was it " + guess["name"])

# checks to see if guess was correct, and ensures correct input
cond = 1
while cond != 0:
    correct = input("")
    correct.lower()
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
    rightAnimal.lower()
    # creates a dict with the string from user and the existing tagList
    animal = {"name" : rightAnimal, "tag" : tagList}
    animalID = "ID" + str(len(answers))
    answerToWrite = {animalID : animal}
    answers.update(answerToWrite)
    # appends new answer to the existing file
    with open('answer.txt', 'w') as fileW:
        fileW.write(json.dumps(answers))
    print("Darn! You got me. Thanks for playing!")