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
    print(f'twoja ocena to: {ocena}')
else:
    print("nieprawidowy wynik")
