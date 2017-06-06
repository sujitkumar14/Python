#about me
import datetime

print('Hello!')
print("How are you")
print('My Name is sujit')
print('Calculate your age')
age = int(raw_input("Enter your year of birth"))
year = datetime.date.today().year
age  = year-age
print("your age is: ")
print(age)
