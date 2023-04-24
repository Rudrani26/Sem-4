def patternCheck(colors, pattern):
    sdict = {}
    colorset = set()
    patternset = set()

    if len(colors) != len(pattern):
        return False

    for i in range(len(pattern)):
        colorset.add(colors[i])
        patternset.add(pattern[i])

        if pattern[i] not in sdict.keys():
            sdict[pattern[i]] = []

        keys = sdict[pattern[i]]
        keys.append(colors[i])
        sdict[pattern[i]] = keys

    if len(patternset) != len(colorset):
        return False

    for values in sdict.values():
        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False
    return True


print(patternCheck(["red", "green", "green"], ["a", "b", "b"]))
print(patternCheck(["red", "green", "greenn"], ["a", "b", "b"]))
