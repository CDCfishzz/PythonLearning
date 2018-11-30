# -*- coding: utf-8 -*-
from io import StringIO, BytesIO

try:
    my_file = open('D:/Users/fishzz/test.txt', 'r', errors='ignore', encoding='utf-8')
    print(my_file.read())
finally:
    if my_file:
        my_file.close()
f_path = 'D:/Users/fishzz/test.txt'
with open(f_path, 'a', encoding='utf-8', errors='ignore') as my_file:
    # print(f.write('\nthis is a write line for test'))
    pass
with open(f_path, 'r', encoding='utf-8', errors='ignore') as my_file:
    print(my_file.read())
    for line in my_file.readlines():
        print(line.strip())

# StringIO
ff = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = ff.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
bf = BytesIO()
# bf = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
bf.write('中文'.encode('utf-8'))
print(bf.getvalue())
