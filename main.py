def dec_to_bin(dec_1):
    dec = int(dec_1)
    print("The given Decimal Number", dec, "in Binary Number is:", bin(dec))

def dec_to_oct(dec_1):
    dec = int(dec_1)
    print("The given Decimal Number", dec, "in Octal Number is:", oct(dec))

def dec_to_hex(dec_1):
    dec = int(dec_1)
    print("The given Decimal Number", dec, "in HexaDecimal Number is:", hex(dec))

def main():
    run = True
    while run:
        print("************************************")
        print("convert.io (Python Number Converter)")
        print("************************************")
        print("_----------------_")
        print("Select your Conversion of choice")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Exit")
        print("_----------------_")
        choice = int(input("Enter your choice (1, 2, 3, 4): "))

        if choice == 1:
            print("_----------------_")
            dec = int(input("Enter the Decimal Number: "))
            dec_to_bin(dec)
            print("_----------------_")
            run = True if input("Continue(y/n): ") == "y" else False
        elif choice == 2:
            print("_----------------_")
            dec = int(input("Enter the Decimal Number: "))
            dec_to_oct(dec)
            print("_----------------_")
            run = True if input("Continue(y/n): ") == "y" else False
        elif choice == 3:
            print("_----------------_")
            dec = int(input("Enter the Decimal Number: "))
            dec_to_hex(dec)
            print("_----------------_")
            run = True if input("Continue(y/n): ") == "y" else False
        elif choice == 4:
            print("Thanks for considering 'convert.io'.")
            break

        if run == False:
            print("Thanks for considering 'convert.io'.")
            break

main()