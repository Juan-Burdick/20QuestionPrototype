#######################################################
# Imports
#######################################################

import json
import random

#######################################################
# FILE I/O
#######################################################

# reads file.txt to store question data in a dict
with open('file.txt', 'r') as fileQ:
    questions = json.load(fileQ)
# sets up a new dict with the same parameters
# to have an editable dict with the questions
unaskedQuestions = dict(questions)
# reads answer.txt to store answer data in a dict
with open('answer.txt', 'r') as fileA:
    answers = json.load(fileA)
# sets up a new dict with the same parameters
# to have an editable dict with the answers
possibleAnswers = dict(answers)

#######################################################
# Variable Declaration
#######################################################

qIndex = 0  # index of currently accessed question
aIndex = 0  # index of answer to guess
iterator = 0  # iterative value
localIterator = 0  # iterator for filling allTags
tagList = []  # list to store question tags to access correct answers
all_yTags = []  # allTags, loaded to check most common tag in answers
yTagRarity = [0]*20  # sibling to allTags, contains rarity of each tag
temp = {}  # for data transfer in dict format
tempList = []  # for data transfer in list format
delValue = {}  # for removal

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
        loopPart = 1  # used to determine which subsection of loop to be operating
        temp.clear()  # clear dict for a new temporary data set
        delValue.clear()  # dict of answers to remove from guess set
        neededUpdate = 1  # for determining if the dict needed updating
        # update the running list of possible answers
        # @param possibleAnswers
        while localIterator <= (len(possibleAnswers)):
            # iterate through answers so we can check tag similarity
            ans = possibleAnswers["ID" + str(localIterator)]

            # loop part 1 populates the delValue array
            if (localIterator <= len(possibleAnswers)) and (loopPart == 1):
                # determines how many explicit dissimilarities the
                # currently accessed answer has from the tagList
                strike = 0
                subLocalIterator = 0  # reset iterator for use
                # check each answer against all tags in tagList
                # add to delValue for removal if dissimilarities >= 4
                while subLocalIterator < len(tagList):
                    tag = tagList[subLocalIterator]
                    if strike >= 4:
                        # create a temporary dict to match top-level fileType
                        aTemp = {"ID" + str(localIterator): ans}
                        delValue.update(aTemp)
                        break  # it already failed, no need to check the rest
                    elif tag not in ans["tag"]:
                        strike += 1  # found an error, increment strikes
                    subLocalIterator += 1  # move the iterator
                localIterator += 1  # move the iterator
                # have we reached the end of the while loop?
                # If so, reset and move to second part of loop
                if localIterator == (len(possibleAnswers)):
                    localIterator = 1
                    loopPart = 2
                    print(delValue)
            # loop part 2 uses delValue to remove
            # selected answers from possibleAnswers
            if (localIterator <= len(possibleAnswers)) and (loopPart == 2):
                subLocalIterator = 0  # reset iterator for use
                # used to acknowledge the skipped index for the value we removed
                skipPoint = 0
                # loop for each answer to be removed in delValue
                if bool(delValue):
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
                    neededUpdate = 0  # didn't need update
                    localIterator += 1 # move the iterator
            elif localIterator == (len(possibleAnswers)):
                if neededUpdate == 1:
                    possibleAnswers = dict(temp)  # load temp into possible answers
                localIterator += 1  # we're done, iterate to exit
                print(possibleAnswers)

        localIterator = 1  # reset iterator for use
        tempList.clear()  # empty list for use
        # populate allTag list and initialize empty tagRarity list
        while localIterator <= len(unaskedQuestions):
            # load all questions so we can access the tags
            curQ = unaskedQuestions["question" + str(localIterator)]
            tempList.append(curQ["yTag"])  # append tag for current question to allTags
            localIterator += 1  # move the iterator

        localIterator = 0  # reset iterator for use
        tempIndex = 0  # index to store removal index for populating tag rarity
        while localIterator < len(all_yTags):
            if localIterator > len(tempList):
                tempIndex = localIterator
            elif all_yTags[localIterator] != tempList[localIterator]:
                tempIndex = localIterator
        all_yTags.clear()
        all_yTags = list(tempList)
        print(all_yTags)  # debugging prints
        yTagRarity.pop(tempIndex)

        localIterator = 0  # reset iterator for use
        tempList.clear()  # empty list for use
        # populate tempList with most recent rarity updates
        while localIterator < len(all_yTags):
            tempList.append(0)
            subLocalIterator = 0  # reset for use
            # for current answer, increment rarity for all tags that it has
            while subLocalIterator < len(possibleAnswers):
                # access all possibleAnswers to check their tags
                ans = possibleAnswers["ID" + str(subLocalIterator + 1)]
                # only increment rarity if the tag appears
                if all_yTags[localIterator] in ans["tag"]:
                    tempList[localIterator] += 1
                subLocalIterator += 1  # move the iterator
            localIterator += 1  # move the iterator

        localIterator = 0  # reset iterator for use
        # merge tempList updates into tagRarity
        while localIterator < len(yTagRarity):
            yTagRarity[localIterator] += tempList[localIterator]
            localIterator += 1
        print(yTagRarity)  # debugging prints

        localIterator = 0  # reset iterator for use
        indexOfMostCommon = 0  # used to keep track of the most common tag
        greatest = 0  # used to find the most common tag
        # find index of most common tag so it's accessible from the allTags list
        while localIterator < len(yTagRarity):
            # if current tag's rarity is higher than greater, replace greater and save index
            if yTagRarity[localIterator] > greatest:
                greatest = yTagRarity[localIterator]
                indexOfMostCommon = localIterator
            localIterator += 1  # move the iterator

        localIterator = 1  # reset iterator for use
        # get the question associated with the most common tag
        while localIterator <= len(unaskedQuestions):
            # look through questions for the one associated with our tag
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
    # force correct input and add associated tag to tagList
    while cond != 0:
        answer = input("")
        answer.lower()  # to standardize input
        if answer == "yes":
            # adds yesTag associated with question to list
            tagList.append(questionCurrent["yTag"])
            cond = 0
        elif answer == "no":
            # adds noTag associated with question to list
            tagList.append(questionCurrent["nTag"])
            cond = 0
        else:
            print("Please enter a valid input. [yes] or [no]")

    localIterator = 1  # reset iterator for use
    temp.clear()  # clear dict for a new temporary data set
    # used to acknowledge the skipped index for the question we remove
    skipPoint = 0
    # update the running list of usable questions
    while localIterator <= len(unaskedQuestions):
        q = unaskedQuestions["question" + str(localIterator)]

        # if q isn't the 'current question'
        # and we haven't found the 'current question'
        # add q to the temporary dict
        if (q is not questionCurrent) and (skipPoint == 0):
            qTemp = {"question" + str(localIterator) : q}
            temp.update(qTemp)
        elif q is questionCurrent:
            skipPoint = 1  # found 'current question', acknowledge skipped index
        # found current q, now offset all elements by one to fill the missed index
        elif (q is not questionCurrent) and (skipPoint == 1):
            qTemp = {"question" + str(localIterator - 1): q}
            temp.update(qTemp)

        localIterator += 1  # move the iterator
    unaskedQuestions = dict(temp)  # load temp into unaskedQuestions

    iterator += 1  # move the iterator

#######################################################
# Selecting guesses, receiving input, and adding to answers
#######################################################

# Select guesses and receive correct input

localIterator = 1  # reset iterator for use
subLocalIterator = 0  # reset iterator for use
loopPart = 1  # used to determine which subsection of loop to be operating
temp.clear()  # clear dict for a new temporary data set
# update the running list of possible answers
# for the final time before guessing
while localIterator <= (len(possibleAnswers) + 1):
    # iterate through answers so we can check tag similarity
    ans = possibleAnswers["ID" + str(localIterator)]
    # dict of answers to remove from guess set
    delValue = {}

    # loop part 1 populates the delValue array
    if (localIterator <= len(possibleAnswers)) and (loopPart == 1):
        # tracks how many diff the current answer has from tagList
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
        # if we've reached end of loop, reset and go to loop part 2
        if localIterator == (len(possibleAnswers) + 1):
            localIterator = 1
            loopPart = 2
    # loop part 2 uses delValue to remove selected answers from possibleAnswers
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
                    # found toDelete, offset remaining elements by one to fill gap
                    if (ans is not toDelete) and (skipPoint == 1):
                        aTemp = {"ID" + str(localIterator - 1): ans}
                        temp.update(aTemp)
                    subLocalIterator += 1  # move the iterator
        localIterator += 1  # move the iterator
    elif localIterator == (len(possibleAnswers) + 1):
        possibleAnswers = dict(temp)  # load temp into possible answers
        localIterator += 1  # we're done, iterate to exit

# randomly selects an answer from possibleAnswers
for y in range(1):
    aIndex = random.randint(0, len(possibleAnswers))
guess = (answers["ID" + str(aIndex)])
print("Was it " + guess["name"])

# checks to see if guess was correct, and ensures correct input
endCond = 0
while endCond == 0:
    correct = input("")
    correct.lower()  # standardizes input
    if correct == "yes":
        print("I knew it! Thanks for playing.")
        endCond = 1  # we were right, exit without editing
    elif correct == "no":
        endCond = -1  # we were wrong, get the right answer from user
    else:
        print("Please enter a valid input. [yes] or [no]")

    ###################################################
    # Select guesses and receive correct input

# adds answer to array if guess was wrong
if endCond == -1:
    # gets animal from user
    print("What was the animal?")
    rightAnimal = input("")
    rightAnimal.lower()  # standardizes input
    localIterator = 1  # reset iterator for use
    exists = 0  # variable to avoid adding a duplicate answer

    # check to see if answer already exists, and update it if so
    while localIterator <= len(answers):
        ans = answers["ID" + str(localIterator)]
        if rightAnimal == ans["name"]:  # answer already exists, update it
            animal = {"tag": tagList}  # add tags to update set
            ans.update(animal)  # update accessed answer
            exists = 1  # animal already exists, don't add a new one
        localIterator += 1  # move the iterator
    # if answer doesn't already exist,
    # creates a dict with
    # @param name: the string from user
    # @param tag: list of the existing tagList
    if exists == 0:
        animal = {"name": rightAnimal, "tag": tagList}  # create a temp dict
        animalID = "ID" + str(len(answers))  # generate new answer's ID
        answerToWrite = {animalID : animal}  # create dict to add
        answers.update(answerToWrite)  # append new answer to file

    # rewrite all answers, including new answer, to the existing file
    with open('answer.txt', 'w') as fileW:
        fileW.write(json.dumps(answers))
    print("Darn! You got me. Thanks for playing!")