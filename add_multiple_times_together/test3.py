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
    print(convert_seconds_into_time(377700))
