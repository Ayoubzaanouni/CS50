answers=["42","Forty Two".lower(),"forty-two".lower()]
answer=input("enter : ").lower().strip()
if answer in answers:
    print("Yes")
else:
    print("No")