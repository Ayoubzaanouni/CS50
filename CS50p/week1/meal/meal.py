def main():
    time = convert(input("time: "))
    if(7<=time<8):
        print("breakfast time")
    elif(12<=time<=13):
        print("lunch time")
    elif(18<=time<19):
        print("dinner time")

def convert(time):
    time = time.lower().strip()
    index = time.find(":")
    hours = float(time[0:index])
    minutes = float(time[index+1:])
    return (hours+minutes/60)


if __name__ == "__main__":
    main()