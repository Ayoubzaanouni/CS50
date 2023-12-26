# TODO
from cs50 import get_string


# count_letters
def count_letters(text):
    len_text = len(text)
    letters = 0
    for i in range(len_text):
        if text[i].isalpha():
            letters = letters+1
    return letters


# count words by spaces
def count_words(text):
    len_text = len(text)
    if (len_text == 0):
        return 0
    else:
        words = 1
        for i in range(len_text):
            if text[i] == " ":
                words = words+1
        return words


# count sentences by points
def count_sentences(text):
    len_text = len(text)
    sentences = 0
    for i in range(len_text):
        if(text[i] == "." or text[i] == "?" or text[i] == '!'):
            sentences = sentences + 1
    return sentences


# main
def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    l = 100 * letters / words
    s = 100 * sentences / words
    # average
    index = round((0.0588 * l) - (0.296 * s) - 15.8)
    if (index < 1):
        print("Before Grade 1\n")
    elif (index >= 16):
        print("Grade 16+\n")
    else:
        print("Grade "+str(index)+"\n")


main()