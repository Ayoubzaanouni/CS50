greeting = input("enter: ")
greets = greeting.lower().strip().split()
if("hello," in greets or "hello"in greets):
    print("$0")
elif(greeting.lower()[0]=='h'):
    print("$20")
else:
    print("$100")