# TODO
from cs50 import get_int


def main():
    credit_card = [int(x) for x in str(get_int("Number: "))]
    test_name = check_name(credit_card)
    if(test_name != "INVALID" and validate(credit_card)):
        print(test_name)
    else:
        print("INVALID")


def check_name(credit_card):
    len_c = len(credit_card)
    two_digit = int(str(credit_card[0])+str(credit_card[1]))
    if(len_c == 15 and (two_digit == 34 or two_digit == 37)):
        return "AMEX"
    elif(len_c == 16 and (two_digit in [51, 52, 53, 54, 55])):
        return "MASTERCARD"
    elif((len_c == 13 or len_c == 16) and credit_card[0] == 4):
        return "VISA"
    else:
        return "INVALID"


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(credit_card):
    # reverse the credit card number
    credit_card = credit_card[::-1]
    # convert to integer
    credit_card = [int(x) for x in credit_card]
    # double every second digit

    double_2_digit = list()
    digits = list(enumerate(credit_card, start=1))

    for index, digit in digits:
        if index % 2 == 0:
            double_2_digit.append(digit * 2)
        else:
            double_2_digit.append(digit)

    # add the digits if any number is more than 9
    double_2_digit = [sum_digits(x) for x in double_2_digit]
    # sum all digits
    sum_of_digits = sum(double_2_digit)
    # return True or False
    return sum_of_digits % 10 == 0


if __name__ == "__main__":
    main()
