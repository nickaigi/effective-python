from time import localtime, strftime 

def example_one():
    """
    >>> 
    2014-08-10 21:18:30
    """
    now = 1407694710

    local_tuple = localtime(now)
    time_format = '%Y-%m-%d %H:%M:%S'
    time_str = strftime(time_format, local_tuple)
    print(time_str)


def main():
    example_one()


if __name__ == '__main__':
    main()
