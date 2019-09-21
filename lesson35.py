# -*- coding: utf-8 -*-
# Base64
import base64
b1 = base64.b64encode(b'binary\x00string')
print(b1)
d1 = base64.b64decode(b1)
print(d1)


def safe_base64_decode(s):
    s = s + b'='*(4 - len(s) % 4)
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')