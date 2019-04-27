import tracemalloc
import waste_memory


def example_one():
    """
      File "/home/mutwa/projects/effective_python_tips/item_59/waste_memory.py", line 7
        self.x = os.urandom(100)
      File "/home/mutwa/projects/effective_python_tips/item_59/waste_memory.py", line 14
        obj = MyObject()
      File "/home/mutwa/projects/effective_python_tips/item_59/waste_memory.py", line 22
        deep_values.append(get_data())
      File "with_trace.py", line 9
        x = waste_memory.run()
      File "with_trace.py", line 18
        example_one()
      File "with_trace.py", line 22
        main()


    - notes for Nick
        - a stack trace like this is most valuable for figuring out which
          particular usage of a common function is responsible for memory consumption in a program.
    """
    tracemalloc.start(10)

    time1 = tracemalloc.take_snapshot()
    x = waste_memory.run()
    time2 = tracemalloc.take_snapshot()
    stats = time2.compare_to(time1, 'traceback')
    top = stats[0]
    print('\n'.join(top.traceback.format()))



def main():
    example_one()


if __name__ == '__main__':
    main()
