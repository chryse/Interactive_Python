def convert_units(money, name):
    result = str(money) + " " + name
    if money > 1:
        result = result + "s"
    return result

def convert(money):
    dollars = int(money)
    cents = int(round(100 * (money - dollars)))
    
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")
    
    if dollars == 0 and cents == 0:
        return "Broke"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string 

def main():
    print convert(11.23)
    print convert(11.20) 
    print convert(1.12)
    print convert(12.01)
    print convert(1.01)
    print convert(0.01)
    print convert(1.00)
    print convert(0)
    


if __name__ == "__main__" :
    main()    
    