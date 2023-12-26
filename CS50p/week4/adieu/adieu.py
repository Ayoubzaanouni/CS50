import inflect

p = inflect.engine()
names =[]
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        adieu_names = p.join(names)
        print('Adieu, adieu, to',adieu_names)
        break