import json
a= {"x":[1,2], "y":(3,4)}
print(a)

with open("data.json","w") as write_file:
    json.dump(a, write_file)

