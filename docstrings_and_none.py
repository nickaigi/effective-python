from datetime import datetime
import time
import json


def log(message, when=None):
    """ Log a message with a timestamp.
    Args:
        message: Message to be printed.
        when: datetime of when the message occured.
            Defaults to present time
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (message, when))


def decode(data, default=None):
    """ Load JSON data from a string

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


if __name__ == '__main__':
    log('Hi')
    time.sleep(1)
    log('Hi again!')

    foo = decode('bad data')
    foo['stuff'] = 5
    bar = decode('also bad')
    bar['meep'] = 1

    print('Foo:', foo)
    print('Bar:', bar)
