def convert(word):
    if(word==':)'):
        return '🙂'
    elif(word==':('):
        return '🙁'
    else:
        return word

def main():
    words = input("input :").strip().split()
    words1=[]
    for word in words:
        words1.append(convert(word))
    words = ' '.join(words1)
    print(words)

main()