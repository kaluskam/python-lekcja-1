wynik=input("Hello student podaj wynik:")
wynik=float(wynik)
ocena=None
if wynik>=0 and wynik<=100:
    if wynik<50:
        ocena=2
    elif wynik<60:
        ocena=3
    elif wynik<70:
        ocena=4
    elif wynik<80:
        ocena=5
    else:
        ocena=6

    print(f"twoja ocena to {ocena}")
else:
    print("nieprawidowy wynik")


age=int(input("how old are you?"))
if age>=18:
    print("adult")
else:
    print("teenager")

def print_day_type():
    day=input("provide a day: ")
    if day=="saturday" or day=="sunday":
        print("weekend")
    else:
        print("weekday")

print_day_type()