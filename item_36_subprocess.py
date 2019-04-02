import subprocess
import time


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


def main():
    # proc = subprocess.Popen(
    #     ['echo', 'Hello from the child!'],
    #     stdout=subprocess.PIPE
    # )

    # out, err = proc.communicate()
    # print(out.decode('utf-8'))

    # proc = subprocess.Popen(['sleep', '0.3'])
    # while proc.poll() is None:
    #     print('Working...')

    # print('Exit status', proc.poll())
    start = time.time()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()
    end = time.time()

    print('Finished in %.3f seconds' % (end - start))


if __name__ == '__main__':
    main()
