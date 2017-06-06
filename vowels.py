#count vowels
vowels =  ['a','e','i','o','u']
s = raw_input('Enter a string: ');
count = 0
for i in range(len(s)):
    if s[i] in vowels:
        count = count +1
print count
