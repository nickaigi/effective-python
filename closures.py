# program to deepen my understanding on how closures work
# A closure occurs when a function has access to a local variable from an
# enclosing scope that has finished its execution.


def echo_msg(msg):
    """ Note
    - we have a nested function
    """
    def act_on_echo():
        print(msg)

    # we returning the name of the function without parenthesis
    return act_on_echo


def multipy_num(n):
    print('multipy_num received: ', n)

    def multipy_by_num(k):
        print('multipy_by_num received: ', k)
        return n * k
    return multipy_by_num


if __name__ == '__main__':
    # assign the return value of the outer function to a variable
    act_one = echo_msg('Welcome to act 1')
    # add parenthesis to the variable to trigger the closure
    act_one()

    # function factories
    five = multipy_num(5)  # multiply_num received: 5
    ten = multipy_num(10)  # multiply_num received: 10

    print(five(2))  # multipy_by_num received: 2
    #  10
    print(ten(5))  # multipy_by_num received: 5
    # 50
