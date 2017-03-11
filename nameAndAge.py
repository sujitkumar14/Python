import datetime
name = raw_input("Enter your name:")
age  = int(raw_input("Enter your age"));
now  = datetime.datetime.now();
print int(now.year)-age+100;
