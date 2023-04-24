# radius = int(input("Enter the radius: "))
# area = 3.14 * radius * radius

# print("Area of Cirle is : ", area)

# ------------------------------------------------------------------------

# fname = input("Enter the first name: ")
# lname = input("Enter the last name: ")

# print("Hello " + lname + " " + fname)

# ------------------------------------------------------------------------

# values = input("Input comma seperated numbers: ")

# list = values.split(",")
# tuple = tuple(list)

# print(list)
# print(tuple)

# ------------------------------------------------------------------------

# color_list = ['Red', 'Green', 'Black', 'Blue']

# print(color_list[0], color_list[-1])

# ------------------------------------------------------------------------

# n = int(input("Enter n : "))

# sum = n + (n*n) + (n*n*n)

# print(sum)

# ------------------------------------------------------------------------

# words = input("Enter comma seperated words: ")

# sepWords = [word for word in words.split(",")]
# print(",".join(sorted(list(set(sepWords)))))

# list = words.split(",")

# print(sorted(list))
# print(sorted(list, reverse=True))

# ------------------------------------------------------------------------

str1 = "I want to spereate each word from this sentence"
print(str1.split(" "))

str1 = "I-want-to-spereate-each-word-from-this-sentence"
print(str1.split("-"))
