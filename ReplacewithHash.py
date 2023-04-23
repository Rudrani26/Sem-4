def replaceWithHash(text):

    for i in text.split():
        if len(i) >= 5:
            text = text.replace(i, "#" * len(i))
    return text


print(replaceWithHash("My name is Rudrani Yojak Chavarkar"))
