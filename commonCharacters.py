import collections


def commonCharacters(str1, str2):
    d1 = collections.Counter(str1)
    d2 = collections.Counter(str2)

    commonChars = d1 & d2

    if len(commonChars) == 0:
        return "No common characters"

    commonCharacters = list(commonChars.elements())
    commonCharacters = sorted(commonCharacters)
    return ''.join(commonCharacters)


print(commonCharacters("Rudrani", "Upadnya"))
print(commonCharacters("xyz", "Upa"))
