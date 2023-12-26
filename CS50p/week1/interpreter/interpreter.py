calculer = input("Expression : ").lower().strip()
index = calculer.find(" ")+1
x = int(calculer[0:calculer.find(" ")])
y = int(calculer[(calculer.find(" ")+2):])
match calculer[index]:
    case '+':
        print(float(x+y))
    case '-':
        print(float(x-y))
    case '/':
        print("%.1f" % float(x/y))
    case '*':
        print(float(x*y))
