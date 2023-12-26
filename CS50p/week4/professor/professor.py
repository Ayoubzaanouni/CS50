import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        trys = 0
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        while trys < 4:
            if trys == 3:
                print(x,'+',y,'=',z)
                break
            print(x,'+',y,'= ',end='')
            answer = input()
            if answer == str(z):
                score+=1
                break
            else:
                print("EEE")
                trys+=1
    print("Score:",score)



def get_level():
    level = -1
    levels =[1,2,3]
    while level not in levels:
        try:
            level = int(input("Level: "))
        except ValueError:
            return get_level()
    return level

def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except:
        raise ValueError
    #x = str(random.randint(0,999))[:level]
    #return int(x)


if __name__ == "__main__":
    main()