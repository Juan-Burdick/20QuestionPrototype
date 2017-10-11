import json

# examples for making and packing questions
print("20q project")

# array to store question tags
tagList = [0]*20
answerList = []

# reads file.txt and stores question dict @param data
with open('file.txt', 'r') as fileQ:
    questions = json.load(fileQ)
print(questions)
# reads answer.txt and stores answers dict
with open('answer.txt', 'r') as fileA:
    answers = json.load(fileA)
print(answers)




count = 0
a = 1



# main while loop of program that asks questions
while count < 20:
    questionCurrent = (questions["question" + str(a)])
    print(questionCurrent["question"])
    cond = 1
    while cond != 0:
        answer = input("")
        if (answer == "yes"):
            tagList[count] = questionCurrent["yTag"]
            cond = 0
        elif (answer == "no"):
            tagList[count] = questionCurrent["nTag"]
            cond = 0
        else:
            print("please enter 'yes' or 'no' ")
    count += 1
    a += 1

print(tagList)


#if count == 20:
#    for ans in answersWriteable:
#        strike = 0
#        for tag in tagList:
#            if strike >= (tagList.len/5):
#                del answersEditable["ans"]
#                break
#            elif tag in ans["tag"]:
#            else:
#                strike += 1


# makes questions with tagList and animal
    # needs if statement to decide if answer
    # exists or needs creation
print("what was the animal")
animal = input("")
answerA = {"ID": '1', animal: tagList}

with open('answer.txt', 'a') as fileW:
    fileW.write(json.dumps(answerA))