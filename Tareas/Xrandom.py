import random
individuos = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
for i in range(5):
    for j in range(5):
        individuos[i][j] = random.randint(0, 1)


for i in range(5):
    for j in range(5):
        if(individuos[i][j] == 0):
            individuos[i+5][j] = 1
        else:
             individuos[i+5][j] = 0

for i in range(10):
    print(individuos[i])