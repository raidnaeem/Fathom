import re
CHAR_NUM = 23107794
WORD_NUM = 4542945
LINE_NUM = 973874


def dict_search():
    dict_file = open("websters-dict.txt", "rb")
    user_word = input("Enter a word: ")
    user_word = user_word.upper()

    # initializing the binary search
    dict_file.seek((int(23107794 / 2)), 0)

    # using regex to find the next entry
    next_word = ""
    match = None
    while not match:
        line = dict_file.readline()
        line = line.decode('utf-8')
        print(line)
        match = re.search(r"[A-Z]+\r?\n", line)
        print(re.search(r"[A-Z]+\r?\n", line))
        if match:
            next_word = match.group()

    print("\nComparisons:")
    if user_word == next_word:
        print("same")
        print("CRAZY!!!!!")
    elif user_word > next_word:
        print("greater")
        print(dict_file.tell())
        dict_file.seek(-(int(dict_file.tell() / 2)), 1)
        print(dict_file.tell())
    elif user_word < next_word:
        print("lesser")
        print(dict_file.tell())
        dict_file.seek(int((CHAR_NUM - dict_file.tell()) / 2), 1)
        print(dict_file.tell())
