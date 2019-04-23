from time import localtime, strftime, mktime, strptime

def example_one():
    """
    >>> 
    2014-08-10 21:18:30
    1407694710.0
    """
    now = 1407694710

    local_tuple = localtime(now)
    time_format = '%Y-%m-%d %H:%M:%S'
    time_str = strftime(time_format, local_tuple)
    print(time_str)

    # End of example one
    # Begin example two

    time_tuple = strptime(time_str, time_format)
    utc_now = mktime(time_tuple)
    print(utc_now)


def main():
    example_one()


if __name__ == '__main__':
    main()
