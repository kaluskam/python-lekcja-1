# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
name=input("Enter your name: ")
age=int(input("Enter your age: "))
age2=input("Enter your age: ")
name2=input("Enter your name2: ")
year_of_birth=int(input("Enter your year of birth: "))
city=input("Enter your city: ")
profession=input("Enter your profession: ")
one_skill_you_want_to_learn=input("Enter your one skill you want to learn: ")
is_car=input("Do you have a car?:(y/n) ").lower().startswith('y')

    # Use a breakpoint in the code line below to debug your script.
print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
print("Hi",',', name,sep='',end='!\n')
print(f'your age is {age}')
print(f'type of age {type(age)}, {age+10}' )
print(f'type of age2 {type(age2)}, {age2+"10"}' )
print(f"Hi,{name2}")
print(f"your year of birth is {year_of_birth}")
print(f"your city is {city}")
print(f"your profession is {profession}")
print(f"your one skill you want to learn is {one_skill_you_want_to_learn}")
if is_car:
    print(f"you have a car")
else:
    print(f'you do not have a car')
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
