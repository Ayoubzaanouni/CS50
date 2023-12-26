application = ["pdf","zip"]
text =["txt"]
image = ["gif","jpg","jpeg","png"]
inp = input("input : ").lower().strip()
i = inp.rfind('.')

subinp =inp[i+1:]

if(subinp in image):
    if(subinp=="jpg"):
        print("image/jpeg")
    else:
        print("image/"+subinp)
elif(subinp in application):
    print("application/"+subinp)
elif(subinp in text):
    print("text/plain")
else:
    print("application/octet-stream")