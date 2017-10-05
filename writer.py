import json

# question dicts
q1 = {"question": "does it have fur", "yTag": "fur", "nTag": "nofur"}
q2 = {"question": "does it eat meat", "yTag": "carni/omni", "nTag": "herbivore"}
q3 = {"question": "does it have a tail", "yTag": "tail", "nTag": "notail"}
q4 = {"question": "dies it fly", "yTag": "fly", "nTag": "notfly"}
q5 = {"question": "does it live in water", "yTag": "water", "nTag": "land/air"}
q6 = {"question": "does it live on land", "yTag": "land", "nTag": "water/air"}
q7 = {"question": "is it a reptile", "yTag": "reptile", "nTag": "notreptile"}
q8 = {"question": "does it a mammal", "yTag": "mammal", "nTag": "notmammal"}
q9 = {"question": "can it climb trees", "yTag": "climber", "nTag": "noclimb"}
q10 = {"question": "does it breath water", "yTag": "gills", "nTag": "no gills"}
q11 = {"question": "is it bigger than or the same size as a dog", "yTag": "biggerthandog", "nTag": "smallerthandog"}
q12 = {"question": "is it active at night", "yTag": "nocturnal", "nTag": "daytime"}
q13 = {"question": "does it live primarily in africa", "yTag": "africa", "nTag": "notafrica"}
q14 = {"question": "is it domesticated", "yTag": "domestic", "nTag": "wild"}
q15 = {"question": "is it a herbavore", "yTag": "herbivore", "nTag": "carni/omni"}
q16 = {"question": "can it shed skin", "yTag": "shedSkin", "nTag": "noShedSkin"}
q17 = {"question": "can it ride a skateboard", "yTag": "rideskateboard", "nTag": "noskateboard"}
q18 = {"question": "does it live in the us", "yTag": "unitedstates", "nTag": "notunitedstates"}
q19 = {"question": "does it have a good sense of smell", "yTag": "goodatsmell", "nTag": "badatsmell"}
q20 = {"question": "does it have echo location", "yTag": "echolocator", "nTag": "noecholocator"}



# making a dict of dicts for file storage
questions = {"question1": q1, "question2": q2, "question3": q3, "question4": q4,
             "question5": q5, "question6": q6, "question7": q7, "question8": q8,
             "question9": q9, "question10": q10, "question11": q11, "question12": q12,
             "question13": q13, "question14": q14, "question15": q15, "question16": q16,
             "question17": q17, "question18": q18, "question19": q19, "question20": q20}

print(questions)

# writes question dict to file.txt
with open('file.txt', 'w') as fileW:
     fileW.write(json.dumps(questions))