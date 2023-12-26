import sys
import inflect
from datetime import date, datetime

i = inflect.engine()

def main():
    birthdate = input("Date of Birth: ")
    validDate = validate_date(birthdate)
    days_difference = calc_difference(validDate)
    output = text(days_difference)
    print(output)


def calc_difference(days):
    today = date.today()
    daysDiff = today - days
    return daysDiff.days * 24 * 60

def validate_date(birthdate):
    try:
        input = date.fromisoformat(birthdate)
        return input
    except ValueError:
        sys.exit("Invalid date")

def text(text):
    text = i.number_to_words(text, andword="")
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()


