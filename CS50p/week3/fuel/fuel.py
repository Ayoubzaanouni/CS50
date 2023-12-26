class x_greater_then_y(Exception):
    pass

while True:
    try:
        fuel = input("Fraction: ").split("/")
        x = int(fuel[0])
        y = int(fuel[1])
        if(x > y):
            raise x_greater_then_y
        if(y == 0):
            raise  ZeroDivisionError
    except ValueError:
        pass
    except x_greater_then_y:
        pass
    else:
        try:
            fuel = float(x)/float(y)
        except  ZeroDivisionError:
            pass
        else:
            fuel = round(fuel*100)
            if(fuel <=1):
                print("E")
            elif(fuel >= 99):
                print("F")
            else:
                print(f"{fuel}%", sep='')
        break