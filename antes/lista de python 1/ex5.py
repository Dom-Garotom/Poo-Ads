sequency = [0,1]

for i in range(8):
    sequency.append(sequency[i] + sequency[i+1])

print(sequency)