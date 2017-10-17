import json
import random

# reads file.txt and stores question data in a dict
with open('file.txt', 'r') as fileQ:
    questions = json.load(fileQ)
print(questions)
# sets up a new dict with same parameters to have an editable dict with the questions
unaskedQuestions = dict(questions)
# reads answer.txt and stores answer data in a dict
with open('answer.txt', 'r') as fileA:
    answers = json.load(fileA)
print(answers)
# sets up a new dict with same parameters to have an editable dict with the answers
possibleAnswers = dict(answers)

tagList = [0]*20  # list to store question tags to access correct answers
answerList = []  # list to store possible answers pulled from doc
alreadyAskedID = []  # list of question IDs to prevent asking same q
alreadyAsked_yTag = []  # list of tags already asked
alreadyAsked_yTagRarity = []  # list for rarity of already asked tags
qIndex = 0  # index of currently accessed question
iterator = 0  # iterative value
all_yTags = []  # allTags, loaded to check most common tag in answers
all_nTags = []  # allTags, loaded to check most common tag in answers
yTagRarity = []  # sibling to allTags, contains rarity of each tag
nTagRarity = []  # sibling to allTags, contains rarity of each tag
tagIterator = 0  # iterator for filling allTags
aIndex = 0  # index of answer to guess
temp = {}  # for data transfer

########################################################

print("Welcome to my home. I believe " +
      "that I can guess what you are thinking.")
# main while loop of program that asks questions
while iterator < 20:
    # randomly generate the first 5 questions to get a baseline
    if iterator < 2:
        # generates a random index for a question to be accessed
        for x in range(1):
            qIndex = random.randint(1, len(unaskedQuestions))

    # intelligently select the remaining questions
    elif 2 <= iterator < 20:

        # TODO: ensure most common tag question doesn't get re-asked

        tagIterator = 1  # reset for use
        temp.clear()  # clear for a new data set
        # add all questions to temp except the one we just saw
        while tagIterator <= len(possibleAnswers):
            a = possibleAnswers["ID" + str(tagIterator)]
            if a is not questionCurrent:
                qTemp = {"question" + str(tagIterator): q}
                temp.update(qTemp)
            tagIterator += 1
        unaskedQuestions = dict(temp)



        tagIterator = 1  # reset iterator for use
        subTagIterator = 0  # reset iterator for use
        loopPart = 1  # used to determine which subsection of loop to be operating
        temp.clear()
        # update the running list of possible answers
        while tagIterator <= len(possibleAnswers):
            ans = possibleAnswers["ID" + str(tagIterator)]
            delValue = {}

            if (tagIterator < len(possibleAnswers)) and (loopPart == 1):
                strike = 0
                # check each answer for all tags in tagList
                # pop and break if there are more than 4 errors
                while subTagIterator < len(tagList):
                    tag = tagList[subTagIterator]
                    if strike >= 4:
                        aTemp = {"ID" + str(subTagIterator)}
                        delValue.update(aTemp)
                        break
                    elif tag not in ans["tag"]:
                        strike += 1
                    subTagIterator += 1
                tagIterator += 1
                if tagIterator == len(possibleAnswers):
                    loopPart = 2
            if (tagIterator < len(possibleAnswers)) and (loopPart == 2):
                subTagIterator = 0
                while subTagIterator < len(delValue):
                    toDelete = delValue["ID" + str(subTagIterator)]
                    if ans is not toDelete:
                        aTemp = {"ID" + str(tagIterator): ans}
                        temp.update(aTemp)
                    subTagIterator += 1
                tagIterator += 1



        tagIterator = 0  # reset for use
        # populate allTag list
        while tagIterator < len(unaskedQuestions):
            curQ = unaskedQuestions["question" + str(tagIterator + 1)]
            all_yTags.append(curQ["yTag"])
            yTagRarity.append(0)
            tagIterator += 1
        print(all_yTags)
        print(yTagRarity)

        while True:
            tagIterator = 0  # reset for use
            # generate the rarity of all tags
            while tagIterator < len(possibleAnswers):
                ans = possibleAnswers["ID" + str(tagIterator + 1)]
                subTagIterator = 0  # reset for use
                while subTagIterator < len(all_yTags):
                    # only increment rarity if the tag appears
                    if all_yTags[subTagIterator] in ans["tag"]:
                        yTagRarity[subTagIterator] += 1
                    subTagIterator += 1  # move subIterator
                tagIterator += 1  # move iterator

            tagIterator = 0  # reset iterator so it can be reused
            indexOfMostCommon = 0  # used to keep track of the most common tag
            greatest = 0  # used to find the most common tag
            # find the index of the most common tag
            # so we can access it from the allTags list
            while tagIterator < len(yTagRarity):
                if yTagRarity[tagIterator] > greatest:
                    greatest = yTagRarity[tagIterator]
                    indexOfMostCommon = tagIterator
                tagIterator += 1  # move iterator

            tagIterator = 1  # reset iterator so it can be reused
            # get the question associated with the most common tag
            while tagIterator <= len(unaskedQuestions):
                curQ = unaskedQuestions["question" + str(tagIterator)]
                if all_yTags[indexOfMostCommon] == curQ["yTag"]:
                    qIndex = tagIterator
                tagIterator += 1  # move iterator

            # break if condition is met
            if qIndex not in alreadyAskedID:
                break

        alreadyAskedID.append(qIndex)

    questionCurrent = (unaskedQuestions["question" + str(qIndex)])
    print(str(iterator + 1) + ". " + questionCurrent["question"])
    cond = 1  # variable to ensure correct input
    # force correct input
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

    tagIterator = 1  # reset for use
    temp.clear()  # clear for a new data set
    # add all questions to temp except the one we just saw
    while tagIterator <= len(unaskedQuestions):
        q = unaskedQuestions["question" + str(tagIterator)]
        if q is not questionCurrent:
            qTemp = {"question" + str(tagIterator) : q}
            temp.update(qTemp)
        tagIterator += 1
    unaskedQuestions = dict(temp)


    iterator += 1

# randomly selects an answer in array to guess
for y in range(1):
    aIndex = random.randint(0, len(answers))
guess = (answers["ID" + str(aIndex)])
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
    tagIterator = 1
    exists = 0  # variable to avoid adding a duplicate animal
    # check to see if answer already exists, and update it if so
    while tagIterator <= len(answers):
        ans = answers["ID" + str(tagIterator)]
        if rightAnimal == ans["name"]:
            animal = {"tag": tagList}
            ans.update(animal)
            exists = 1  # animal already exists, don't add a new one
        tagIterator += 1  # move iterator
    # creates a dict with the string from user and the existing tagList
    if exists == 0:
        animal = {"name" : rightAnimal, "tag" : tagList}
        animalID = "ID" + str(len(answers))
        answerToWrite = {animalID : animal}
        answers.update(answerToWrite)
    # appends new answer to the existing file
    with open('answer.txt', 'w') as fileW:
        fileW.write(json.dumps(answers))
    print("Darn! You got me. Thanks for playing!")