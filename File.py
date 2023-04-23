import string
from shutil import copyfile


def file_read(fname):
    txt = open(fname)
    print(txt.read())


file_read('demo.txt')


def file_read(fname):
    with open(fname) as f:
        # Content_list is the list that contains the read lines.
        content_list = f.readlines()
        print(content_list)


file_read('demo.txt')


def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in the file: ", file_lengthy("demo.txt"))

copyfile('demo.txt', 'abc.txt')


def count_words(filepath):
    with open(filepath) as f:
        data = f.read()
        data.replace(",", " ")
    return len(data.split(" "))


print(count_words("demo.txt"))


def letters_file_line(n):
    with open("words1.txt", "w") as f:
        alphabet = string.ascii_uppercase
        letters = [alphabet[i:i + n] +
                   "\n" for i in range(0, len(alphabet), n)]
        f.writelines(letters)


letters_file_line(3)
