import collections

str1 = "rudranichavarkardaughterofyojakchavarkaryolo"

count = collections.defaultdict(int)

for letter in str1:
    count[letter] += 1

for letter in sorted(count, key=count.get, reverse=True):
    if count[letter] > 1:
        print(letter, count[letter])
