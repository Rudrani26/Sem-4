def caesarCipher(inputText, step):
    outputText = []
    cypherText = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in inputText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            cypherLetter = (index + step) % 26
            cypherText.append(cypherLetter)
            outputLetter = uppercase[cypherLetter]
            outputText.append[outputLetter]
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            cypherLetter = (index + step) % 26
            cypherText.append(cypherLetter)
            outputLetter = lowercase[cypherLetter]
            outputText.append(outputLetter)
    return outputText


print(caesarCipher("rudrani", 3))
