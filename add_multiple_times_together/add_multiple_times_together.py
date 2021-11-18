times_needed_to_be_added = ['01:22:15', '1999:10:55']


def add_times(times_list):
    seconds_list = []

    for time_str in times_list:
        hour_minute_second_list = time_str.split(':')
        total_seconds = int(hour_minute_second_list[0]) * 3600 + int(hour_minute_second_list[1]) * 60 + int(
            hour_minute_second_list[2])

        seconds_list.append(total_seconds)

    total_seconds_summed = sum(seconds_list)
    print(total_seconds_summed)
    hours = total_seconds_summed // 3600
    minutes = (total_seconds_summed % 3600) // 60
    seconds = (total_seconds_summed % 3600) % 60
    print(hours, minutes, seconds)


if __name__ == '__main__':
    add_times(times_needed_to_be_added)
