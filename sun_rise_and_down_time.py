import time

file_name = 'rushan_city_data.csv'
new_file_name = 'rushan_city_data_edit.csv'

# Clear the new file.
with open(file=new_file_name, mode='w') as write_file:
    write_file.write('日期,日出,日中,日落,昼长,天亮,天黑,平均\n')

avg_time_str_list = []
with open(file=file_name, mode='r') as file:
    lines_list = file.readlines()
    first_line = lines_list[0]
    lines_list = lines_list[1:]
    for line in lines_list:
        splitted_line_list = line.split(sep=',')
        daybreak_time_str = '1970-1-2 ' + splitted_line_list[-2]
        nightfall_time_str = '1970-1-1 ' + splitted_line_list[-1]
        if nightfall_time_str[-1] == '\n':
            nightfall_time_str = nightfall_time_str[:-1]
        daybreak_struct_time = time.strptime(daybreak_time_str, '%Y-%m-%d %H:%M:%S')
        daybreak_time_stamp = int(time.mktime(daybreak_struct_time))
        nightfall_struct_time = time.strptime(nightfall_time_str, '%Y-%m-%d %H:%M:%S')
        nightfall_time_stamp = int(time.mktime(nightfall_struct_time))
        avg_time_stamp = int((daybreak_time_stamp + nightfall_time_stamp) / 2)
        avg_struct_time = time.localtime(avg_time_stamp)
        avg_date_time_str = time.strftime("%Y-%m-%d %H:%M:%S", avg_struct_time)
        avg_time_str = avg_date_time_str.split(' ')[1]
        avg_time_str_list.append(avg_time_str)
        with open(file=new_file_name, mode='a') as write_file:
            write_file.write(line[:-1] + ',' + avg_date_time_str + '\n')
