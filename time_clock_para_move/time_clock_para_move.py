import time

time_clock_list = ['22:15', '06:30', '10:55', '12:00', '12:15', '13:35', '19:30', '22:15', '22:29']

# How many minutes you want to move earlier or later.
# Minus time for moving to an earlier time, plus time for an later time.
move_time = -90

time_clock_list_new = []

for time_str in time_clock_list:
    time_str_full = '1970-1-2 ' + time_str
    struct_time = time.strptime(time_str_full, '%Y-%m-%d %H:%M')
    time_stamp = int(time.mktime(struct_time))

    time_stamp_new = time_stamp + move_time * 60

    struct_time_new = time.localtime(time_stamp_new)
    time_str_new = time.strftime('%H:%M', struct_time_new)
    time_clock_list_new.append(time_str_new)

with open(file='time_clock_history.txt', mode='a') as file:
    file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ' history:\n')
    file.write('Old time clock list: ' + str(time_clock_list) + '\n')
    file.write('New time clock list: ' + str(time_clock_list_new) + '\n')
    file.write('\n')
