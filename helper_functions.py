from urllib.parse import parse_qs


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


if __name__ == '__main__':
    """ There are multiple clever ways to get the value of the querystring
    variables
    - since the query string param could have multiple values,
      parse_qs returns an array of all the values of the param
    - we are interested in getting the int representation of the first value of
      the param

    option 1: difficult to read
        red = my_values.get('red', [''])[0] or 0

    option 2: use if/else or ternary expression
        red = my_values.get('red', [''])
        red = int(red[0]) if red[0] else 0

        - good, but still not as clear as a full if/else

    option3: full if/else
        green = my_values.get('green', [''])
        if green[0]:
            green = int(green[0])
        else:
            green = 0

    It is good practice to use a helper function, esp if ou need to use this
    logic repeatedly
    """
    my_values = parse_qs(
        'red=5&blue=0&green=',
        keep_blank_values=True
    )
    green = get_first_int(my_values, 'green')
