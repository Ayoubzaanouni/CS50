grocery =[]
gocery_count ={}
while True:
    try:
        item = input().upper()
        grocery.append(item)
    except EOFError:
        grocery.sort()
        for item in grocery:
           gocery_count[item]=grocery.count(item)
        for k in gocery_count:
            print(gocery_count[k],k)
        break
