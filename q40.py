import random
from datetime import datetime

data = list(range(10))

random.shuffle(data)
split = int(0.7 * len(data))

train = data[:split]
test = data[split:]

print("Split time:", datetime.now())
