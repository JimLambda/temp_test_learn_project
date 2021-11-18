# How long you have learned today.
times_needed_to_be_added = ['01:22:15', '1999:10:55']

# Total length of your learning videos or learning materials.
total_time_length_of_your_learning_videos_or_materials = '100:00:00'

# How long you have learned up to yesterday. (Include yesterday. But today's progress is not
# included, today's learning progress should be in times_needed_to_be_added.)
current_progress_time = '00:40:00'


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


if __name__ == '__main__':
    total_seconds_today_learned = add_times(times_needed_to_be_added)
    total_time_today_learned = convert_seconds_into_time(total_seconds_today_learned)

    temp_list = [total_time_today_learned, current_progress_time]
    total_seconds_up_to_now = add_times(temp_list)
    total_time_up_to_now = convert_seconds_into_time(total_seconds_up_to_now)

    with open('learning_progress.txt', mode='a') as file:

