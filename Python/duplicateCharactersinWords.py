def duplicateCharacters(text):
    sepWords = text.split()

    for words in sepWords:
        if len(words) > len(set(words)):
            return False
    return True


print(duplicateCharacters("Filter out the factorials of the said list."))
print(duplicateCharacters("Python Exercise."))
print(duplicateCharacters("lets go"))
