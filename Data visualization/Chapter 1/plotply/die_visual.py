from die import Die

results = []
die = Die()

for i in range(1000):
    result = die.Roll()
    results.append(result)

frequencies = []
for value in range(1, die.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
