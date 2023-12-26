import re

def convert(s):
    # regex pattern for first format (9:00 AM to 5:00 PM)
    pattern1 = r'(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)'
    # regex pattern for second format (9 AM to 5 PM)
    pattern2 = r'(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)'
    # check if input string matches either of the two formats
    match1 = re.search(pattern1, s)
    match2 = re.search(pattern2, s)

    if match1:
        # get hour and minute values from first format
        start_hour = int(match1.group(1))
        start_minute = int(match1.group(2))
        start_meridian = match1.group(3)
        end_hour = int(match1.group(4))
        end_minute = int(match1.group(5))
        end_meridian = match1.group(6)
    elif match2:
        # get hour and minute values from second format
        start_hour = int(match2.group(1))
        start_minute = 0
        start_meridian = match2.group(2)
        end_hour = int(match2.group(3))
        end_minute = 0
        end_meridian = match2.group(4)
    else:
        # input does not match either of the two formats
        raise ValueError("Input must be in one of the two formats")

    # check if the hours and minutes are valid
    if start_hour > 12 or end_hour > 12 or start_minute > 59 or end_minute > 59:
        raise ValueError("Invalid hour or minute")

    # convert to 24-hour format
    if start_meridian == 'PM' and start_hour != 12:
        start_hour += 12
    if end_meridian == 'PM' and end_hour != 12:
        end_hour += 12
    if start_meridian == 'AM' and start_hour == 12:
        start_hour = 0
    if end_meridian == 'AM' and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


def main():
    print(convert(input("Hours: ")))

if __name__ == "__main__":
    main()