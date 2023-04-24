# def duplicateInt(numbers):
#     num_set = set(numbers)

#     return len(numbers) != len(num_set)


# print(duplicateInt([1, 2, 3, 4, 5]))
# print(duplicateInt([1, 1, 2, 3, 4, 5]))

# ---------------------------------------------------------------
import array as arr


# def sepList(numbers):
#     return sorted(set(numbers), key=numbers.index)


# numArray = arr.array('i', [1, 2, 3, 4, 5, 1, 2, 3])

# print("Orginal Array")
# for i in range(len(numArray)):
#     print(numArray[i], end=' ')

# print("\nNew Array")
# numArray = arr.array('i', sepList(numArray))
# for i in range(len(numArray)):
#     print(numArray[i], end=' ')

# ---------------------------------------------------------------

# def findMissingNumber(numbers):
#     return sum(range(10, 21)) - sum(list(numbers))


# numArray = arr.array('i', [10, 11, 12, 13, 14, 15, 16, 18, 19, 20])

# print("Orginal Array")
# for i in range(len(numArray)):
#     print(numArray[i], end=' ')

# print("\nMissing number")
# print(findMissingNumber(numArray))

# ---------------------------------------------------------------

def upperOrlower(str1):
    dict = {"UpperCase": 0, "LowerCase": 0}

    for character in str1:
        if character.isupper():
            dict["UpperCase"] += 1
        elif character.islower():
            dict["LowerCase"] += 1
    print(dict)


upperOrlower("Hello I am Rudrani Chavakar")
