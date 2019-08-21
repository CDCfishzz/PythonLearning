# -*- coding: utf-8 -*-
# 正则表达式
import re

# 正则匹配
tel_num_test = '010-123456'
if re.match(r'^\d{3}-\d{3,8}$', tel_num_test):
    print('ok')
else:
    print('failed')

# 正则切分
split_test = 'a,b;;c  , d   e;, f'
print(re.split(r'[\s,;]+', split_test))

# 正则分组
group_test = re.match(r'(\d{3})-(\d{3,8})', tel_num_test)
# group(0)为原始字符串
for i in range(len(group_test.groups()) + 1):
    print(group_test.group(i))

# 预编译
re_telephone = re.compile(r"^(\d{3})-(\d{3,8})$")

print(re_telephone.match(tel_num_test).groups())


# 邮箱验证
def is_valid_email(addr):
    re_mail = re.compile(r'^(.[\w_.]*)@(\w+)\.(\w+)$')

    if re_mail.match(addr) is None:
        return False
    return re_mail.match(addr).group(1)


print(is_valid_email('_CDCfishzz.test@gmail.com'))
