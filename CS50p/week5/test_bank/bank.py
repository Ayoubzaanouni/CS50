def main():
    print(value(input("enter: ")))
def value(greeting):
    greets = greeting.lower().strip().split()
    if(len(greets) >0):
        if("hello," in greets or "hello"in greets):
            return(0)
        elif(greeting.lower()[0]=='h'):
            return(20)
        else:
            return(100)
    else:
        return

if __name__ == "__main__":
    main()