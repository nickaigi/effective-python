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


def example_two():
    """
    >>> 
    ValueError: time data '2014-05-01 15:45:16 PDT' does not match format '%Y-%m-%d %H:%M:%S %Z'
    """
    parse_format = '%Y-%m-%d %H:%M:%S %Z'
    depart_sfo = '2014-05-01 15:45:16 PDT'
    time_tuple = strptime(depart_sfo, parse_format)
    time_str = strftime(time_format, time_tuple)
    print(time_str) 


def main():
    example_two()


if __name__ == '__main__':
    main()
