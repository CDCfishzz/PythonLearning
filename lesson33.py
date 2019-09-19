# -*- coding: utf-8 -*-
# datetime 模块
import re
from datetime import datetime, timedelta, timezone

dt_test1 = datetime(2019, 9, 20, 12, 24)
print(dt_test1)

# 时间戳
print(dt_test1.timestamp())
t_test1 = 1429417200.0
# 本地时间
print(datetime.fromtimestamp(t_test1))
# UTC时间
print(datetime.utcfromtimestamp(t_test1))

# string & datetime 转换
str_test1 = '2015-6-1 18:42:59'
print(datetime.strptime(str_test1, '%Y-%m-%d %H:%M:%S'))
now = datetime.now()
print(now.strftime('%a, %b %d, %H:%M'))

# datetime加减

now1 = datetime.now()
print(now1)
now1 += timedelta(hours=10)
print(now1)
now1 -= timedelta(days=1)
print(now1)

# local to UTC

tz_utc_8 = timezone(timedelta(hours=8))
now2 = datetime.now()
print(now2)
dt = now2.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转换

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print("BeiJin time:", bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print("Tokyo time:", tokyo_dt)

# 时区转换的关键在于，拿到一个datetime时，
# 要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
# 注：不是必须从UTC+0:00时区转换到其他时区，
# 任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

# 测试


def to_timestamp(dt_str, tz_str):
    dtt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_num = int(re.match(r'^UTC([+-]\d+):00$', tz_str).group(1))
    tz = timezone(timedelta(hours=tz_num))
    utc_dtt = dtt.replace(tzinfo=tz)
    return utc_dtt.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

