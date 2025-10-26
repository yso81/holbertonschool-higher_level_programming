#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, iterable):
        num_items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {num_items_added} items")

    def remove(self, item):
        print(f"Removed {item} from the list")
        super().remove(item)

    def pop(self, index=-1):
        if index < -len(self) or index >= len(self):
            raise IndexError("pop index out of range")
        
        item = self[index]
        print(f"Pop {item} from the list")
        return super().pop(index)


if __name__ == "__main__":
    from task_02_verboselist import VerboseList

    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)