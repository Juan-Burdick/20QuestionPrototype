import json

# question dicts
q1 = {"question": "does it have fur", "yTag": 1, "nTag": 2}
q2 = {"question": "does it eat meat", "yTag": 3, "nTag": 4}
q3 = {"question": "does it have a tail", "yTag": 5, "nTag": 6}
q4 = {"question": "dies it fly", "yTag": 7, "nTag": 8}
q5 = {"question": "does it have a cool face", "yTag": 9, "nTag": 10}
q6 = {"question": "does it have fur", "yTag": 11, "nTag": 12}
q7 = {"question": "does it have fur", "yTag": 13, "nTag": 14}
q8 = {"question": "does it have fur", "yTag": 15, "nTag": 16}
q9 = {"question": "does it have fur", "yTag": 17, "nTag": 18}
q10 = {"question": "does it have fur", "yTag": 19, "nTag": 20}
q11 = {"question": "does it have fur", "yTag": 21, "nTag": 22}
q12 = {"question": "does it have fur", "yTag": 23, "nTag": 24}
q13 = {"question": "does it have fur", "yTag": 25, "nTag": 26}
q14 = {"question": "does it have fur", "yTag": 27, "nTag": 28}
q15 = {"question": "does it have fur", "yTag": 29, "nTag": 30}
q16 = {"question": "does it have fur", "yTag": 31, "nTag": 32}
q17 = {"question": "does it have fur", "yTag": 33, "nTag": 34}
q18 = {"question": "does it have fur", "yTag": 35, "nTag": 36}
q19 = {"question": "does it have fur", "yTag": 37, "nTag": 38}
q20 = {"question": "does it have fur", "yTag": 39, "nTag": 40}



# making a dict of dicts for file storage
questions = {"question1": q1, "question2": q2, "question3": q3, "question4": q4,
             "question5": q5, "question6": q6, "question7": q7, "question8": q8,
             "question9": q9, "question10": q10, "question11": q11, "question12": q12,
             "question13": q13, "question14": q14, "question15": q15, "question16": q16,
             "question17": q17, "question18": q18, "question19": q19, "question20": q20}

print(questions["question1"])
print(questions["question2"])

# writes question dict to file.txt
with open('file.txt', 'w') as fileW:
     fileW.write(json.dumps(questions))