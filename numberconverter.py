def convertDecimal(decimal_number):

    converted_number = ""
    try:
        decimal_number = int(decimal_number)
        while decimal_number > 0:
            # Divides our base ten number by 2, takes the remainder and stores it in the string, then repeats the process on the quotient
            quotient = decimal_number // 2
            remainder = decimal_number % 2

            converted_number += str(remainder)
            decimal_number = quotient
        # Inverts the string for our actual final number
        converted_number = converted_number[::-1]
        return converted_number
    except ValueError:
        return "Something went wrong :( that probably wasn't a number"

def convertBinary(binary_number):
    try:
        converted_number = int(binary_number, 2)
        return converted_number
    except ValueError:
        return "I cant translate that :( it's not a binary number"

if __name__ == "__main__":
    number_type = input("Enter which type of number you would like to convert (Binary, Decimal): ").lower()
    
    if number_type == "binary":
        user_number_output = convertBinary(input("Please input a Binary number: "))
    elif number_type == "decimal": 
        user_number_output = convertDecimal(input("Please input a decimal number: "))
    else:
        user_number_output = "That is not a valid number system."

    print(user_number_output)