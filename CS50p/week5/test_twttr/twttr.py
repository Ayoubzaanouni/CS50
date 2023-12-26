def main():
    print(shorten(input("word: ")))


def shorten(word):
    vowels = ['A','E','I','O','U']
    inp = list(word)
    out = ""
    for i in inp:
        if(i.upper() not in vowels):
            out+=i
    return out


if __name__ == "__main__":
    main()