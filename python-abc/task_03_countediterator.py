#!/usr/bin/python3
"""
Custom iterstor that records the number of items iterated
"""


class CountedIterator:
    """
    extends the built-in iterator obtained from the iter function
    """

    def __init__(self, some_iterable):
        """
        Initialises the CountedIterator with an item
        """
        self.iterator = iter(some_iterable)
        self.count = 0
    
    def get_count(self):
        """
        return the current value of the counter
        """
        return self.count
    
    def __next__(self):
        """
        Gets the next item and increments counter

        Raises:
            StopIteration
        
        Return the next item
        """
        try:
            nxt_item = next(self.iterator)
            self.count += 1
            return nxt_item
        except StopIteration:
            raise
    
    def __iter__(self):
        return self

if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]
    counted_iter = CountedIterator(my_list)

    for item in counted_iter:
        print(f"Item {counted_iter.get_count()}: {item}")
        print(f"Count: {counted_iter.get_count()}")

    print(f"my_list_count: {counted_iter.get_count()}")
    print(f"\n")
    print(f"New list:")
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
    except StopIteration:
        print("No more items.")
