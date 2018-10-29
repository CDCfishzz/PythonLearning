# -*- coding: utf-8 -*-
s1 = 72
s2 = 85
r = s2/s1 - 1
print('%.1f%%' % r)
s3 = ['1', '2', '3']
print(s3[:])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0], L[1][1], L[2][2])

age = 12
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

mySum = 0
for x in range(1, 101):
    mySum += x
print(mySum)


sum2 = 0
n = 99
while n > 0:
    sum2 += n
    n -= 2
print(sum2)
# test this is new change






