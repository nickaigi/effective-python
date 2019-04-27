"""How to pdb
Debugger commands

    - bt: print the traceback of the current execution call stack

    - up: move your scope up the function call stack to the caller of the current
          function

    - down: move your scope back down the function call stack one level

    - step: run the program until the next line of execution in the program
            then return control back to the debugger. If the next line of
            execution includes calling a function, the debugger will stop in
            the function that was called.

    - next: run the program until the next line of execution in the current
            function, then return control back to the debugger. If the next
            line of execution includes calling a function, the debugger will
            not stop until the called function has returned.

    - return: run the program until the current function returns, then return
              control back to the debugger.

    - continue: continue running the program until the next breakpoint
                (or set_trace is called again). Simmillar to pressing 'c'
"""


def complex_func(name, gender, age):
    import pdb; pdb.set_trace()


def main():
    complex_func('nick', 'male', '31')


if __name__ == '__main__':
    main()
