#######################################################
# Imports
#######################################################

import json
import random
import copy

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
iterator = 0  # iterative value
tagList = []  # list to store question tags to access correct answers
deleteThis = []  # list of ids of answers to remove from possible answers

#######################################################
# Functions
#######################################################


# populate the array of ids to delete from possibleAnswers
def populate_delete_this():
    global possibleAnswers  # access global possibleAnswers to see if any of them no longer meet the criteria
    global deleteThis  # global array of ids of answers to remove, populated here and accessed elsewhere
    local_iterator = 1  # iterator

    if len(tagList) >= 4:  # if tagList is shorter than 4, nothing can strike out, so don't bother
        # check each answer to if it strikes out
        while local_iterator <= len(possibleAnswers):
            if check_for_removal(local_iterator):
                # this answer needs to go, add its index to the deleteThis array
                deleteThis.append(("ID" + str(local_iterator)))
            local_iterator += 1  # move the iterator
        # print("possibleAnswers in populate_delete_this: " + str(possibleAnswers))
        # print("deleteThis in populate_delete_this: " + str(deleteThis))


# for the answer at the passed index, return true if it has too many dissimilarities to tagList (default = 4)
def check_for_removal(index):
    global possibleAnswers  # needed to access the answer at passed index
    global tagList  # needed to check tag-sequence similarity
    strikes = 0  # number of tags in tagList that the answer does not have
    local_iterator = 0  # iterator

    ans = possibleAnswers["ID" + str(index)]  # the one answer we're working with

    # for each tag in tagList, check to see if it's in the answer's tags
    while local_iterator < len(tagList):
        tag = tagList[local_iterator]
        if strikes >= 4:  # this answer has 4 strikes, remove it
            return True
        elif tag not in ans["tag"]:  # found a dissimilarity, increment strikes
            strikes += 1
        local_iterator += 1  # move the iterator
    return False  # total strikes were under 4, this answer should stay


# update the running list of possible answers
def update_possible_answers():
    global possibleAnswers  # needed to refresh
    global deleteThis  # needed to know which values to delete
    local_iterator = 0  # iterator
    some_var = (len(possibleAnswers))  # maintains length of possible answers pre-delete for re-sequencing after delete

    if deleteThis:  # only run if there's even anything to delete
        while local_iterator < (len(deleteThis)):  # for each index in deleteThis list
            if (deleteThis[local_iterator]) in possibleAnswers:  # if this index even exists
                del possibleAnswers[deleteThis[local_iterator]]  # delete index corresponding to current index
            local_iterator += 1  # move the iterator
        reindex_possible_answers(some_var)  # compress the indices, pass the old size so the top doesn't get deleted
        # print("possibleAnswers in update_possible_answers: " + str(possibleAnswers))
        # print("deleteThis in update_possible_answers: " + str(deleteThis))


# compress the indices of possible answers so they form a solid sequence from 1-1+
def reindex_possible_answers(old_length):
    global possibleAnswers  # needed to reset
    local_iterator = 1  # iterator
    temp = {}  # temporarily hold re-indexed possibleAnswers
    temp.clear()  # ensure it's clear
    new_indices = 1  # count incremented for each added element to ensure a linear progress of indices
    # print("possibleAnswers in reindex_possible_answers before: " + str(possibleAnswers))

    while local_iterator <= old_length:  # for each element before deletion - ensures we visit every index
        if ("ID" + str(local_iterator)) in possibleAnswers:  # if this element still exists, add it to temp
            ans = possibleAnswers["ID" + str(local_iterator)]  # access the current answer
            temp.update({("ID" + str(new_indices)): ans})  # add current answer to temp with next index in line
            new_indices += 1  # increment for next index to add
        local_iterator += 1  # move the iterator
    possibleAnswers = copy.deepcopy(temp)  # deepcopy to ensure proper transmission of nested dicts
    # print("possibleAnswers in reindex_possible_answers after: " + str(possibleAnswers))


# create a temporary list of tags associated with unasked questions, and their associated rarity
def update_tag_data():
    global unaskedQuestions  # bring in unaskedQuestions to get all tags associated with them
    global possibleAnswers  # bring in possibleAnswers to find the most relevant tag (and associated question)
    local_iterator = 1  # iterator
    index_of_most_common = 0  # index of the most common tag
    all_tags = []  # list of all tags associated with unasked questions, reset whenever function is run
    tag_rarity = []  # list of tag rarities, on a 1-to-1 with all_tags, reset whenever function is run

    all_tags.clear()  # empty list for use
    while local_iterator <= len(unaskedQuestions):  # populate all_tags list
        # load each questions so we can access the associated tags
        current_question = unaskedQuestions["question" + str(local_iterator)]
        all_tags.append(current_question["yTag"])  # append yTag for current question to all_tags
        all_tags.append(current_question["nTag"])  # append nTag for current question to all_tags
        local_iterator += 1  # move the iterator

    local_iterator = 0  # reset the iterator for use
    while local_iterator < len(all_tags):  # populate the tag_rarity list
        tag_rarity.append(0)  # create a new rarity entry for this tag
        temp_iterator = 1  # create a temporary iterator
        while temp_iterator <= len(possibleAnswers):  # check every answer in possibleAnswers
            current_answer = possibleAnswers["ID" + str(temp_iterator)]
            current_answer_tags = list(current_answer["tag"])  # access the tags for currently accessed answer
            sub_iterator = 0  # nested temporary iterator
            # check every tag in currently accessed answer for occurrence of current tag from all_tags
            while sub_iterator < len(current_answer_tags):
                # if we found an instance of the tag, increment the rarity
                if all_tags[local_iterator] == current_answer_tags[sub_iterator]:
                    tag_rarity[local_iterator] += 1
                sub_iterator += 1  # move the iterator
            temp_iterator += 1  # move the iterator
        local_iterator += 1  # move the iterator

    local_iterator = 0  # reset the iterator for use
    while local_iterator < len(tag_rarity):  # find the most common tag
        # if value of current is greater than
        # current greatest, move index
        if tag_rarity[local_iterator] > tag_rarity[index_of_most_common]:
            index_of_most_common = local_iterator
        local_iterator += 1  # move the iterator

    # return the tag at the index with the highest rarity value
    return all_tags[index_of_most_common]


# find the question associated with the passed tag
def select_question(most_common_tag):
    global unaskedQuestions  # bring in unaskedQuestions to compare their tags to most_common_tag
    local_iterator = 1  # iterator

    while local_iterator <= len(unaskedQuestions):  # get index for question associated with most common tag
        # look through questions for the one associated with our tag
        current_question = unaskedQuestions["question" + str(local_iterator)]
        # if the currently accessed question's yTag is the most common tag, return this index
        if current_question["yTag"] == most_common_tag:
            return local_iterator
        # if the currently accessed question's nTag is the most common tag, return this index
        elif current_question["nTag"] == most_common_tag:
            return local_iterator
        local_iterator += 1  # move the iterator
    return 1  # if something breaks and index isn't found, return 1 by default


# update the running list of unasked questions by removing the most recently asked question
def update_unasked_questions(index_of_just_asked):
    global unaskedQuestions  # needed to remove latest question
    local_iterator = 1  # iterator
    temp = {}  # temporarily holds re-indexed unaskedQuestions
    temp.clear()  # ensures dict is clear for new data
    new_indices = 1  # count incremented for each added element to ensure a linear progress of indices

    del unaskedQuestions[("question" + str(index_of_just_asked))]  # delete the most recent question
    while local_iterator <= (len(unaskedQuestions) + 1):  # access each question, and add 1 bc our dict shortened
        if ("question" + str(local_iterator)) in unaskedQuestions:  # if this element still exists, add it to temp
            question = unaskedQuestions["question" + str(local_iterator)]  # access the current question
            temp.update({("question" + str(new_indices)): question})  # add current q to temp with next index in line
            new_indices += 1  # increment for next index to add
        local_iterator += 1  # move the iterator
    unaskedQuestions = copy.deepcopy(temp)  # deepcopy to ensure proper transmission of nested dicts
    # print("unaskedQuestions: " + str(unaskedQuestions))


#######################################################
# Main execution: While loop
#######################################################

print("Welcome to the game. I believe " +
      "that I can guess what you are thinking.")

# main while loop of program that asks questions
while iterator < 20:
    # randomly generate the first 3 questions to get a baseline
    if iterator < 3:
        # generates a random index for a question to be accessed
        for x in range(1):
            qIndex = random.randint(1, len(unaskedQuestions))

    # intelligently select the remaining questions
    elif 3 <= iterator < 20:
        deleteThis.clear()  # clear deleteThis for a new data set
        populate_delete_this()  # re-populate deleteThis
        update_possible_answers()  # update the running list of possible answers
        mostCommonTag = update_tag_data()  # find the most common tag
        qIndex = select_question(mostCommonTag)  # get the index of the question associated with the most common tag

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
    # print(tagList)
    update_unasked_questions(qIndex)  # updates the running list of unasked questions

    iterator += 1  # move the iterator

#######################################################
# Selecting guesses, receiving input, and adding to answers
#######################################################

# Select guesses and receive correct input
deleteThis.clear()  # clear deleteThis for a new data set
populate_delete_this()  # re-populate deleteThis
update_possible_answers()  # update the running list of possible answers

endCond = 0  # variable to determine if new data needs to be acquired and/or added
# randomly selects an answer from possibleAnswers
if len(possibleAnswers) == 0:  # if there is nothing left in possibleAnswers, we've already lost, go to collecting data
    print("Well I'm stumped!")
    endCond = -1
else:  # possibleAnswers exists, select a random answer from it
    aIndex = 0  # variable for storing the random number
    for y in range(1):  #RNG
        aIndex = random.randint(0, len(possibleAnswers))
    guess = (possibleAnswers["ID" + str(aIndex)])  # sets answer to guess
    print("Was it " + guess["name"])  # prints out final answer

    # checks to see if guess was correct, and ensures correct input
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
    print("What was the animal?")  # gets animal from user
    rightAnimal = input("")  # input line
    rightAnimal.lower()  # standardizes input
    localIterator = 1  # iterator
    exists = 0  # variable to avoid adding a duplicate answer

    # check to see if answer already exists, and update it if so
    while localIterator <= len(answers):  # check all answers
        ans = answers["ID" + str(localIterator)]
        if rightAnimal == ans["name"]:  # answer already exists, update it
            animal = {"tag": tagList}  # add tags to update set
            ans.update(animal)  # update accessed answer
            exists = 1  # animal already exists, don't add a new one
        localIterator += 1  # move the iterator
    # if answer doesn't exist, create dict with
    # @param name: the string from user
    # @param tag: list of the existing tagList
    if exists == 0:
        animal = {"name": rightAnimal, "tag": tagList}  # create a temp dict
        animalID = "ID" + str(len(answers) + 1)  # generate new answer's ID, put it at the end of dict
        answerToWrite = {animalID : animal}  # create dict to add
        answers.update(answerToWrite)  # append new answer to file

    # rewrite all answers, including new answer, to the existing file
    with open('answer.txt', 'w') as fileW:
        fileW.write(json.dumps(answers))
    print("Darn! You got me. Thanks for playing!")
