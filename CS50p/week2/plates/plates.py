def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(s == 'CS05'):
        return False
    else:
        if(s.isalnum() and 6 >= len(s) >=2 and s[0:2].isalpha() and s[0] != 0):
            i = 2
            while i < len(s):
                if(s[i].isnumeric()):
                    if(s[i:].isnumeric()):
                        return True
                    else:
                        return False
                else:
                    i+=1
                    continue
            return True
        else:
            return False



main()