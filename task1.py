class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        #self.outer_index = -1
        self.inner_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Если внешний индекс превысил длину списка, останавливаем итерацию
        if self.outer_index >= len(self.list_of_list):
            raise StopIteration
        
        # Если внутренний индекс превысил длину вложенного списка, перемещаемся на следующий внешний список
        if self.inner_index >= len(self.list_of_list[self.outer_index]):
            self.outer_index += 1
            self.inner_index = 0
            return self.__next__()

        # Возвращаем текущий элемент и увеличиваем внутренний индекс
        item = self.list_of_list[self.outer_index][self.inner_index]
        self.inner_index += 1
        return item

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()