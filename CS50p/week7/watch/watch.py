import re

def main():
    print(parse(input("HTML: ")))

def parse(s):

    if src := re.search(r'src=[\'"]([^\'"]+)', s):
        src = src.group(1)
        you = re.search(r'(youtube)', src)
        if you:
            id = re.sub(r"^(https?://)?(www\.)?youtube\.com/([a-z0-9_]+)", "", src)
            return f"https://youtu.be"+id
        else:
            return None


if __name__ == "__main__":
    main()