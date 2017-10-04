import json

# examples for making and packing questions
print("20q project")

# array to store question tags
tagList = [0]*20

# reads file.txt and stores question dict @param data
with open('file.txt', 'r') as fileR:
    questions = json.load(fileR)

count = 0
a = 1


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


