import string
variable = list(input("camelCase: "))
snake = ""
alphabet = list(string.ascii_uppercase)

for i in variable:
    if(i not in alphabet):
        snake+=i
    else:
        snake = snake+'_'+i.lower()

print("snake_case: "+snake)
