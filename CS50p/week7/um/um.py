import re



def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(re.compile(r'\bum\b', re.IGNORECASE), s))
if __name__ == "__main__":
    main()