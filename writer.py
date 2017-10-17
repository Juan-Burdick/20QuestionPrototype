import json

# question dicts
q1 = {"question": "Does it have fur?", "yTag": "fur", "nTag": "noFur"}
q2 = {"question": "Does it eat meat?", "yTag": "carnivore/omnivore", "nTag": "herbivore"}
q3 = {"question": "Does it have a tail?", "yTag": "tail", "nTag": "noTail"}
q4 = {"question": "Can it fly?", "yTag": "canFly", "nTag": "cantFly"}
q5 = {"question": "Does it mostly live in water?", "yTag": "water", "nTag": "land/air"}
q6 = {"question": "Is it an amphibian?", "yTag": "amphibian", "nTag": "notAmphibian"}
q7 = {"question": "Is it a reptile?", "yTag": "reptile", "nTag": "notReptile"}
q8 = {"question": "Is it a mammal?", "yTag": "mammal", "nTag": "notMammal"}
q9 = {"question": "Can it climb trees?", "yTag": "climbsTrees", "nTag": "notClimbTrees"}
q10 = {"question": "Does it breath water?", "yTag": "gills", "nTag": "notGills"}
q11 = {"question": "Is it bigger than a dog?", "yTag": "biggerThanDog", "nTag": "smallerThanDog"}
q12 = {"question": "Is it active at night?", "yTag": "nocturnal", "nTag": "daytime"}
q13 = {"question": "Does it live primarily in Africa?", "yTag": "africa", "nTag": "notAfrica"}
q14 = {"question": "Is it domesticated?", "yTag": "domestic", "nTag": "wild"}
q15 = {"question": "Does it have hooves?", "yTag": "hooves", "nTag": "notHooves"}
q16 = {"question": "Can it shed its skin?", "yTag": "shedSkin", "nTag": "noShedSkin"}
q17 = {"question": "Can it fit on a skateboard?", "yTag": "fitsOnSkateboard", "nTag": "doesntFitOnSkateboard"}
q18 = {"question": "Does it live primarily in North America?", "yTag": "inNA", "nTag": "notInNA"}
q19 = {"question": "Does it have a good sense of smell?", "yTag": "goodAtSmell", "nTag": "badAtSmell"}
q20 = {"question": "Does it have echo location?", "yTag": "echoLocation", "nTag": "noEchoLocation"}
q21 = {"question": "Is it native to snowy regions?", "yTag": "snow", "nTag": "notSnow"}
q22 = {"question": "Is it a fish?", "yTag": "fish", "nTag": "notFish"}
q23 = {"question": "Is it a bird?", "yTag": "bird", "nTag": "notBird"}
q24 = {"question": "Can it swim?", "yTag": "swim", "nTag": "cantSwim"}
q25 = {"question": "Does it have legs?", "yTag": "legs", "nTag": "notLegs"}






# making a dict of dicts for file storage
questions = {"question1": q1, "question2": q2, "question3": q3, "question4": q4,
             "question5": q5, "question6": q6, "question7": q7, "question8": q8,
             "question9": q9, "question10": q10, "question11": q11, "question12": q12,
             "question13": q13, "question14": q14, "question15": q15, "question16": q16,
             "question17": q17, "question18": q18, "question19": q19, "question20": q20,
             "question21": q21, "question22": q22, "question23": q23, "question24": q24,
             "question25": q25}

print(questions)

# writes question dict to file.txt
with open('file.txt', 'w') as fileW:
     fileW.write(json.dumps(questions))