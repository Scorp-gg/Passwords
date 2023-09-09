import random
while True:
    low = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symbol = "[}{}()*;/,._-@#$"

    T = low + upper + num + symbol
    l = input("Enter the desired length: ")

    try:
        inte = int(l)
        if isinstance(inte,int):
            password = "".join(random.sample(T,inte))
            print(f"Generated password: {password}")
            new = input("Generate new password?S/N")
            if new.upper() == "N":
                break
    except ValueError:
        try:
            flt=float(l)
            print("Enter a valid number")
        except ValueError:
            print("Enter a valid number")

