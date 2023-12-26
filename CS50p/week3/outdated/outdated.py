months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

def main():
    date = get_date()
    print(date)

def get_date():
    while True:
        date = input8("Date: ").strip()
        try:
            if (',') in date and ("/") not in date:
                date = date.split(', ')
                year = date[1]
                monthDay = date[0].split(" ")
                day = monthDay[1].zfill(2)
                monthIndex = months.index(monthDay[0]) + 1

                if int(day) > 31:
                    return get_date()
                f_date = f"{year}-{monthIndex:02}-{day:02}"
                return f_date

            elif ('/') in date:
                if date.isalnum():
                    return get_date()

                date = date.split('/')

                for x in date:
                    if " " in x:
                        return get_date()

                month = date[0].zfill(2)
                day = date[1].zfill(2)
                year = date[2]

                if int(day) > 31 or int(month) > 12:
                    return get_date()

                f_date = f"{year}-{month}-{day}"
                return f_date
            else:
                return get_date()
        except:
            return get_date()
main()