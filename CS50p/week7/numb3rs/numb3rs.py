import re

def main():
    print(validate(input("IPV4 Address: ").strip()))

def validate(ip):
    ip_len = ip.split('.')
    if len(ip_len) != 4:
        return False
    else:
        if (re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)):
            return True
        else:
            return False


if __name__ == "__main__":
    main()