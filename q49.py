import random
import statistics

data = list(range(20))

sample = random.sample(data, 5)

print("Sample:", sample)
print("Mean:", statistics.mean(sample))
