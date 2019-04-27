"""Memory management in CPython, uses reference counting. This ensures that
as soon as all references to an object have expired, the referenced object is
cleared.

CPython has a built-in cycle detector to ensure that self-referencing objects
are eventually garbage collected
"""


import gc
import waste_memory


def example_one():
    """
    5165 objects before
    15178 objects after
    <waste_memory.MyObject object at 0x7f2b059c4518>
    <waste_memory.MyObject object at 0x7f2b059c4550>
    <waste_memory.MyObject object at 0x7f2b059c4588>


    - notes for Nick
        - the problem with g.get_objects is that it doesn't tell you anything
          about how the objects were allocated.
    """
    found_objects = gc.get_objects()
    print('%d objects before' % len(found_objects))
    x = waste_memory.run()
    found_objects = gc.get_objects()
    print('%d objects after' % len(found_objects))

    for obj in found_objects[:3]:
        print(repr(obj)[:100])




def main():
    example_one()


if __name__ == '__main__':
    main()
