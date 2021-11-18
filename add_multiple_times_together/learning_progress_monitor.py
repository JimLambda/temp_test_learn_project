import time

# How long you have learned up to yesterday. (Include yesterday. But today's progress is not
# included, today's learning progress should be in times_needed_to_be_added.)
current_progress_time = '00:00:00'

# How long you have learned today.
times_needed_to_be_added = ['00:00:01']

# Total length of your learning videos or learning materials.
total_time_length_of_your_learning_videos_or_materials = '27:54:16'


def convert_time_into_seconds(time_str: str):
    """
    Convert time str into seconds. Such as: '01:00:00' into 3600.

    :param time_str: Time str. For example: '01:00:00'.
    :return: Seconds. Integer.
    """
    hour_minute_second_list = time_str.split(':')
    total_seconds = int(hour_minute_second_list[0]) * 3600 + int(hour_minute_second_list[1]) * 60 + int(
        hour_minute_second_list[2])
    return total_seconds


def add_times(times_list: list):
    """
    Sum up time in times_list.

    :param times_list: For example: ['01:22:15', '1999:10:55'], with time string inside the list.
    :return: Total seconds summed by all times in the times_list.
    """
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
    # print(hours, minutes, seconds)
    return total_seconds_summed


def convert_seconds_into_time(seconds_needed_to_be_converted: int):
    """
    Convert total seconds integer into time string, such as: 3600 into '01:00:00'.

    :param seconds_needed_to_be_converted: Seconds, should be an integer.
    :return: Time str, str. For example: '01:00:00'.
    """
    hours = seconds_needed_to_be_converted // 3600
    minutes = (seconds_needed_to_be_converted % 3600) // 60
    seconds = (seconds_needed_to_be_converted % 3600) % 60
    print(hours, minutes, seconds)
    time_str = str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)
    return time_str


def calculate_percentage(num: int, total_num: int):
    """
    Percentage, num / total_num.

    :param num: Integer.
    :param total_num: Integer.
    :return: Percentage, str.
    """
    percentage = (num / total_num) * 100
    return format(percentage, '.1f')


if __name__ == '__main__':
    total_length_seconds = convert_time_into_seconds(total_time_length_of_your_learning_videos_or_materials)

    total_seconds_today_learned = add_times(times_needed_to_be_added)
    percentage_today = calculate_percentage(total_seconds_today_learned, total_length_seconds)
    total_time_today_learned = convert_seconds_into_time(total_seconds_today_learned)

    temp_list = [total_time_today_learned, current_progress_time]
    total_seconds_up_to_now = add_times(temp_list)
    total_time_up_to_now = convert_seconds_into_time(total_seconds_up_to_now)
    percentage_up_to_now = calculate_percentage(total_seconds_up_to_now, total_length_seconds)

    with open('learning_progress.txt', mode='a') as file:
        file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ' history:\n')
        file.write('Today added:\t{}\n'.format(times_needed_to_be_added))
        file.write('Today learned:\t{}\t{}%\tTotal length:{}\n'.format(total_time_today_learned, percentage_today,
                                                                       total_time_length_of_your_learning_videos_or_materials))
        file.write('Up to today:\t{}\t{}%\n\n'.format(total_time_up_to_now, percentage_up_to_now))
