import json
import random

#######################################################
# FILE I/O
#######################################################

# reads file.txt to store question data in a dict
with open('file.txt', 'r') as fileQ:
    questions = json.load(fileQ)
print(questions)
# sets up a new dict with the same parameters
# to have an editable dict with the questions
unaskedQuestions = dict(questions)
# reads answer.txt to store answer data in a dict
with open('answer.txt', 'r') as fileA:
    answers = json.load(fileA)
print(answers)
# sets up a new dict with the same parameters
# to have an editable dict with the answers
possibleAnswers = dict(answers)

#######################################################
# Variable Declaration
#######################################################

tagList = [0]*20  # list to store question tags to access correct answers
alreadyAskedID = []  # list of question IDs to prevent asking same q
alreadyAsked_yTag = []  # list of tags already asked
alreadyAsked_yTagRarity = []  # list for rarity of already asked tags
qIndex = 0  # index of currently accessed question
iterator = 0  # iterative value
all_yTags = []  # allTags, loaded to check most common tag in answers
all_nTags = []  # allTags, loaded to check most common tag in answers
yTagRarity = []  # sibling to allTags, contains rarity of each tag
nTagRarity = []  # sibling to allTags, contains rarity of each tag
localIterator = 0  # iterator for filling allTags
aIndex = 0  # index of answer to guess
temp = {}  # for data transfer

#######################################################
# Main execution: While loop
#######################################################

print("Welcome to the game. I believe " +
      "that I can guess what you are thinking.")
# main while loop of program that asks questions
while iterator < 20:
    ###################################################
    # Selector (random at first, then semi-intelligent)

    # randomly generate the first 5 questions to get a baseline
    if iterator < 5:
        # generates a random index for a question to be accessed
        for x in range(1):
            qIndex = random.randint(1, len(unaskedQuestions))

    # intelligently select the remaining questions
    elif 5 <= iterator < 20:

        localIterator = 1  # reset iterator for use
        subLocalIterator = 0  # reset iterator for use
        loopPart = 1  # used to determine which subsection of loop to be operating
        temp.clear()  # clear dict for a new temporary data set
        # update the running list of possible answers
        # @param possibleAnswers
        while localIterator <= (len(possibleAnswers) + 1):
            # iterate through answers so we can check tag similarity
            ans = possibleAnswers["ID" + str(localIterator)]
            # dict of answers to remove from guess set
            delValue = {}
            # loop part 1 populates the delValue array
            if (localIterator <= len(possibleAnswers)) and (loopPart == 1):
                # determines how many explicit dissimilarities the
                # currently accessed answer has from the tagList
                strike = 0
                # check each answer against all tags in tagList
                # add to delValue for removal if dissimilarities >= 4
                while subLocalIterator < len(tagList):
                    tag = tagList[subLocalIterator]
                    if strike >= 4:
                        # create a temporary dict to match top-level fileType
                        aTemp = {"ID" + str(subLocalIterator): ans}
                        delValue.update(aTemp)
                        break  # it already failed, no need to check the rest
                    elif tag not in ans["tag"]:
                        strike += 1  # found an error, increment strikes
                    subLocalIterator += 1  # move the iterator
                localIterator += 1  # move the iterator
                # have we reached the end of the while loop?
                # If so, reset and move to second part of loop
                if localIterator == (len(possibleAnswers) + 1):
                    localIterator = 1
                    loopPart = 2
            # loop part 2 uses delValue to remove
            # selected answers from possibleAnswers
            if (localIterator <= len(possibleAnswers)) and (loopPart == 2):
                subLocalIterator = 0  # reset iterator for use
                # used to acknowledge the skipped index for the value we removed
                skipPoint = 0
                # loop for each answer to be removed in delValue
                while subLocalIterator < len(delValue):
                    toDelete = delValue["ID" + str(subLocalIterator)]
                    # as long as answer isn't toDelete
                    # and we haven't found toDelete yet
                    # add answer to temporary array
                    if (ans is not toDelete) and (skipPoint == 0):
                        aTemp = {"ID" + str(localIterator): ans}
                        temp.update(aTemp)
                    elif ans is toDelete:
                        skipPoint = 1  # found toDelete, acknowledge skipped index
                    # we found toDelete, now offset all added elements
                    # by one so we can fill the missed index
                    if (ans is not toDelete) and (skipPoint == 1):
                        aTemp = {"ID" + str(localIterator - 1): ans}
                        temp.update(aTemp)
                    subLocalIterator += 1  # move the iterator
                localIterator += 1  # move the iterator
            else:
                break  # something went wrong, exit anyway

        localIterator = 1  # reset iterator for use
        # populate allTag list and initialize empty tagRarity list
        while localIterator <= len(unaskedQuestions):
            # load all questions so we can access the tags
            curQ = unaskedQuestions["question" + str(localIterator)]
            all_yTags.append(curQ["yTag"])  # append tag for current question to allTags
            yTagRarity.append(0)  # append initial rarity of 0 for current question
            localIterator += 1  # move the iterator
        print(all_yTags)  # debugging prints
        print(yTagRarity)  # debugging prints

        localIterator = 0  # reset iterator for use
        # populate tagRarity with actual rarities
        while localIterator < len(possibleAnswers):
            # access all possibleAnswers to check their tags
            ans = possibleAnswers["ID" + str(localIterator + 1)]
            subLocalIterator = 0  # reset for use
            # for currently accessed answer,
            # increment all rarities for tags that it has
            while subLocalIterator < len(all_yTags):
                    # only increment rarity if the tag appears
                    if all_yTags[subLocalIterator] in ans["tag"]:
                        yTagRarity[subLocalIterator] += 1
                    subLocalIterator += 1  # move the iterator
            localIterator += 1  # move the iterator

        localIterator = 0  # reset iterator for use
        indexOfMostCommon = 0  # used to keep track of the most common tag
        greatest = 0  # used to find the most common tag
        # find the index of the most common tag
        # so we can access it from the allTags list
        while localIterator < len(yTagRarity):
                # if the currently accessed tag's rarity is higher
                # than our current, replace current and save index
                if yTagRarity[localIterator] > greatest:
                    greatest = yTagRarity[localIterator]
                    indexOfMostCommon = localIterator
                localIterator += 1  # move the iterator

        localIterator = 1  # reset iterator for use
        # get the question associated with the most common tag
        while localIterator <= len(unaskedQuestions):
                # sequentially access questions until
                # we find the one associated with our tag
                curQ = unaskedQuestions["question" + str(localIterator)]
                if all_yTags[indexOfMostCommon] == curQ["yTag"]:  # found it
                    qIndex = localIterator  # set our qIndex to this
                    break  # found it, no need to keep looking
                localIterator += 1  # move the iterator

    ###################################################
    # Print question, receive input, reduce unanswered questions

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

    localIterator = 1  # reset for use
    temp.clear()  # clear for a new data set
    skipPoint = 0  # found question we just used, skip it
    # add all questions to temp except the one we just saw
    while localIterator <= len(unaskedQuestions):
        q = unaskedQuestions["question" + str(localIterator)]
        if (q is not questionCurrent) and (skipPoint == 0):
            qTemp = {"question" + str(localIterator) : q}
            temp.update(qTemp)
        elif q is questionCurrent:
            skipPoint = 1
        elif (q is not questionCurrent) and (skipPoint == 1):
            qTemp = {"question" + str(localIterator - 1): q}
            temp.update(qTemp)
        localIterator += 1
    unaskedQuestions = dict(temp)

    iterator += 1

#######################################################
# Selecting guesses, receiving input, and adding to answers
#######################################################

    ###################################################
    # Select guesses and receive correct input

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

    ###################################################
    # Select guesses and receive correct input

# adds answer to array if guess was wrong
if cond == 0:
    # gets animal from user
    print("What was the animal?")
    rightAnimal = input("")
    rightAnimal.lower()
    localIterator = 1
    exists = 0  # variable to avoid adding a duplicate animal
    # check to see if answer already exists, and update it if so
    while localIterator <= len(answers):
        ans = answers["ID" + str(localIterator)]
        if rightAnimal == ans["name"]:
            animal = {"tag": tagList}
            ans.update(animal)
            exists = 1  # animal already exists, don't add a new one
        localIterator += 1  # move iterator
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