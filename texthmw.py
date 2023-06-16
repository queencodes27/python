from collections import Counter

with open('data.txt', 'r') as f:
    data = f.read().splitlines()

# split each line into key and value, and count the number of occurrences
key_counts = Counter([line.split(',')[0] for line in data])

# get the 10 most common keys and their counts
for key, count in key_counts.most_common(10):
    print(key, count)
