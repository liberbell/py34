scores = {"math": 30,
          "science": 40,
          "english": 80,
          "society": 40
          }

print(scores)
print(type(scores))

print(scores["math"])
scores["physics"] = 100
print(scores)

scores.pop("physics")
print(scores)