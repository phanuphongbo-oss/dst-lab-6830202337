def convert_currency(amount,type):
    if type == "usd":
        result = amount * 32.8
        print(f"{amount} = {result:.2f}")
    else :
        result = amount / 32.8
        print(f"{amount} = {result:.2f}")



convert_currency(100,"usd")
convert_currency(100,"")

