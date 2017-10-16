import json

# ID dicts
a1 = {"name": "cat", "tag": []}
a2 = {"name": "dog", "tag": []}
a3 = {"name": "bat", "tag": []}
a4 = {"name": "giraffe", "tag": []}
a5 = {"name": "shark", "tag": []}
a6 = {"name": "ostrich", "tag": []}
a7 = {"name": "rabbit", "tag": []}
a8 = {"name": "fish", "tag": []}
a9 = {"name": "bird", "tag": []}
a10 = {"name": "hawk", "tag": []}
a11 = {"name": "whale", "tag": []}
a12 = {"name": "rhino", "tag": []}
a13 = {"name": "hippo", "tag": []}
a14 = {"name": "elephant", "tag": []}
a15 = {"name": "panda", "tag": []}
a16 = {"name": "tiger", "tag": []}
a17 = {"name": "lion", "tag": []}
a18 = {"name": "cheetah", "tag": []}
a19 = {"name": "snake", "tag": []}
a20 = {"name": "viper", "tag": []}
a21 = {"name": "gazelle", "tag": []}
a22 = {"name": "deer", "tag": []}
a23 = {"name": "moose", "tag": []}
a24 = {"name": "bear", "tag": []}



# making a dict of dicts for file storage
answers = {"ID1": a1, "ID2": a2, "ID3": a3, "ID4": a4,
           "ID5": a5, "ID6": a6, "ID7": a7, "ID8": a8,
           "ID9": a9, "ID10": a10, "ID11": a11, "ID12": a12,
           "ID13": a13, "ID14": a14, "ID15": a15, "ID16": a16,
           "ID17": a17, "ID18": a18, "ID19": a19, "ID20": a20,
           "ID21": a21, "ID22": a22, "ID23": a23, "ID24": a24}

print(answers)

# writes ID dict to file.txt
with open('answer.txt', 'w') as fileW:
     fileW.write(json.dumps(answers))