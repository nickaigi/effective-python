from time import localtime, strftime, mktime, strptime
from datetime import datetime, timezone
import pytz


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
    time_str = strftime(parse_format, time_tuple)
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


def example_four():
    """
    >>> 
    1407658710.0
    """
    time_format = '%Y-%m-%d %H:%M:%S'
    time_str = '2014-08-10 11:18:30'
    now = datetime.strptime(time_str, time_format)
    time_tuple = now.timetuple()
    utc_now = mktime(time_tuple)
    print(utc_now)


def example_five():
    """
    >>> 
    2014-05-02 03:33:24+00:00
    """
    time_format = '%Y-%m-%d %H:%M:%S'
    arrival_nyc = '2014-05-01 23:33:24'
    nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
    eastern = pytz.timezone('US/Eastern')
    nyc_dt = eastern.localize(nyc_dt_naive)
    utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
    print(utc_dt)


def main():
    example_two()


if __name__ == '__main__':
    main()
