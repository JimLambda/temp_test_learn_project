import time

str1 = '1970-1-1 23:40:00'

print(time.strptime(str1, '%Y-%m-%d %H:%M:%S'))
struct_time = time.strptime(str1, '%Y-%m-%d %H:%M:%S')

timeStamp = int(time.mktime(struct_time))
print(timeStamp)

timestamp = 1462451334

# 转换成localtime
time_local = time.localtime(timestamp)
# 转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

print(dt)
