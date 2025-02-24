def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        return "Freezing"
    if 0<temp<=10:
        return "Very Cold"
    if 11<=temp<20:
        return "Cold"
    if 20<=temp<30:
        return "Normal"
    if 30<=temp<40:
        return "Hot"
    if temp>=40:
        return "Hot"
print(main(43))