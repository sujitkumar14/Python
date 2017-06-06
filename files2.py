#file creation
import os
os.chdir(r'C:\Users\sujit\Desktop')
try:
    os.makedirs('test-folder')
except Exception:
    pass
os.chdir(r'C:\Users\sujit\Desktop\test-folder')
print(os.getcwd())
with open('test.txt','w') as f:
    f.write('sujit')
with open('test.txt','r') as f:
    print(f.read())

