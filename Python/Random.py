import random
import string

print("#{:06x}". format(random.randint(0, 0xFFFFFF)))

print(random.choice(string.ascii_letters))

maxLen = 255
s = ''
for i in range(maxLen):
    s += random.choice(string.ascii_letters)
print(s)

s = ''
for i in range(10):
    s += random.choice(string.ascii_letters)
print(s)

print(random.randint(23, 35))

print(random.randint(0, 10) * 7)

print(random.Random().random())
print(random.Random(0).random())
print(random.random())

elements = range(0, 100)
randElements = random.sample(elements, 10)
print(randElements)
listElements = list(random.sample(randElements, 5))
print(listElements)
