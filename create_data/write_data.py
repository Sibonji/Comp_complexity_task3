import random
import math as mt
import json

random.seed(1)

n = 12

points = {}
for i in range(n):
    points[i] = (random.randint(1,1000), random.randint(1,1000))

json_text = json.dumps(points)
print(json_text)
with open('data.json', 'w') as f:
    json.dump(json_text, f)