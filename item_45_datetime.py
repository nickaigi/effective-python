from time import localtime, strftime, mktime, strptime
from datetime import datetime, timezone

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


def example_three():
    """
    >>> 
    2014-08-10 21:18:30+03:00
    """
    now = datetime(2014, 8, 10, 18, 18, 30)
    now_utc = now.replace(tzinfo=timezone.utc)
    now_local = now_utc.astimezone()
    print(now_local)


def main():
    example_three()


if __name__ == '__main__':
    main()
