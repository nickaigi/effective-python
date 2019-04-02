import os
import time
import subprocess


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Q13S\x11'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    proc.stdin.write(data)
    proc.stdin.flush()  # Ensure the child gets input
    return proc


def example_one():
    proc = subprocess.Popen(
        ['echo', 'Hello from the child!'],
        stdout=subprocess.PIPE
    )

    out, err = proc.communicate()
    print(out.decode('utf-8'))


def example_two():
    proc = subprocess.Popen(['sleep', '0.3'])
    while proc.poll() is None:
        print('Working...')

    print('Exit status', proc.poll())


def example_three():
    start = time.time()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()
    end = time.time()

    print('Finished in %.3f seconds' % (end - start))


def example_four():
    procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = run_openssl(data)
        procs.append(proc)

    for proc in procs:
        out, err = proc.communicate()
        print(out[-10:])


def run_md5(input_stdin):
    """ NOTE
    Python's hashlib built-in module provides the md5 function, so running a
    subprocess like this isn't always nescessary. The goal here is to
    demonstrate how subprocesses can pipe inputs and outputs.
    """
    proc = subprocess.Popen(
        ['md5sum'],
        stdin=input_stdin,
        stdout=subprocess.PIPE,
    )
    return proc


def example_five():
    input_procs = []
    hash_procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = run_openssl(data)
        input_procs.append(proc)
        hash_proc = run_md5(proc.stdout)
        hash_procs.append(hash_proc)

    for proc in input_procs:
        proc.communicate()
    for proc in hash_procs:
        out, err = proc.communicate()
        print(out.strip())


def main():
    example_five()


if __name__ == '__main__':
    main()
