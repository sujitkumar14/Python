import sys
s  = raw_input().strip()
for i in range(0,len(s)):
    if s[i].islower():
        sys.stdout.write(s[i].upper())
    else:
        sys.stdout.write(s[i].lower())
