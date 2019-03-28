""" Python implements its container behaviours with instance methods that
have special names.

>>> bar = [1, 2, 3]
>>> bar[0]

Will be interpreted as

>>> bar.__getitem__(0)

implementing __getitem__ isn't enough to provide all the sequence semantics
you'd expect

>>> len(tree)
>>> TypeError: object of type 'IndexableNode' has no len()

The len built-in fx requires special method __len__
your custom type must implement __len__

This still isn't enough. We expect to have count() and index() on a sequence like a list or tuple

Thankfully, python has collections.abc module

>>> class BadType(Sequence):
>>>    pass
>>> foo = BadType()
>>> TypeError
"""


from collections.abc import Sequence


class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class IndexableNode(BinaryNode):
    def _search(self, count, index):
        found = None
        if self.left:
            found, count = self.left._search(count, index)
        if not found and count == index:
            found = self
        else:
            count += 1
        if not found and self.right:
            found, count = self.right._search(count, index)
        return found, count

    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value


class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count


class BetterNode(SequenceNode, Sequence):
    pass


def main():
    # foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
    # print('Length is ', len(foo))
    # foo.pop()
    # print('After pop ', repr(foo))
    # print('Frequency:', foo.frequency())

    # tree = IndexableNode(
    #     10,
    #     left=IndexableNode(
    #         5,
    #         left=IndexableNode(2),
    #         right=IndexableNode(
    #             6,
    #             right=IndexableNode(7)
    #         )
    #     ),
    #     right=IndexableNode(
    #         15, left=IndexableNode(11)
    #     )
    # )

    # print('LRR = ', tree.left.right.right.value)
    # print('Index 0 = ', tree[0])
    # print('Index 1 = ', tree[1])
    # print('11 in the tree?', 11 in tree)
    # print('17 in the tree?', 17 in tree)
    # print('Tree is ', list(tree))


    # tree = SequenceNode(
    #     10,
    #     left=IndexableNode(
    #         5,
    #         left=IndexableNode(2),
    #         right=IndexableNode(
    #             6,
    #             right=IndexableNode(7)
    #         )
    #     ),
    #     right=IndexableNode(
    #         15, left=IndexableNode(11)
    #     )
    # )
    # print('The tree has %d nodes' % len(tree))

    tree = BetterNode(
        10,
        left=IndexableNode(
            5,
            left=IndexableNode(2),
            right=IndexableNode(
                6,
                right=IndexableNode(7)
            )
        ),
        right=IndexableNode(
            15, left=IndexableNode(11)
        )
    )
    print('Index of 7 is ', tree.index(7))
    print('Count of 10 is ', tree.count(10))
    

if __name__ == '__main__':
    main()
