# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bmi = weight/height**2
bmiI = 1
bmiT = ['过轻', '正常', '过重', '肥胖', '严重肥胖']
if bmi <= 18.5:
    bmiI = 0
elif bmi <= 25:
    bmiI = 1
elif bmi <= 28:
    bmiI = 2
elif bmi <= 32:
    bmiI = 3
else:
    bmiI = 4
print('你的BMI值为%.2f,体型%s' % (bmi, bmiT[bmiI]))

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,%s!' % x)
