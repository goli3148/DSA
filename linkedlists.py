class List:
    def __init__(self, init_data=None):
        if init_data:
            self._data_ = init_data
        else:
            self._data_ = []

    def insert(self, data):
        self._data_.append(data)

    def delete(self, index=-1):
        self._data_.pop(index)
    
    def search(self, value):
        for index, data in enumerate(self._data_):
            if data == value:
                return index
        return None
    
    def get(self, index):
        return self._data_[index]   
    
    def merge_sorted(self, list: 'List'):
        final_data = []
        start_index1 = 0
        start_index2 = 0
        while True:
            if self._data_[start_index1] <= list._data_[start_index2]:
                final_data.append(self._data_[start_index1])
                start_index1 += 1
            else:
                final_data.append(list._data_[start_index2])
                start_index2 += 1
            if start_index1 == len(self._data_):
                final_data.extend(list._data_[start_index2:])
                break
            if start_index2 == len(list._data_):
                final_data.extend(self._data_[start_index1:])
                break
        return final_data
    

class Operations:
    def merged_sort(self, lists: list[List]):
        final_data = []
        start_indices = [0 for _ in range(len(lists))]
        while True:
            if len(start_indices) == 0:
                return final_data
            gather = [list.get(start_indices[index]) for index, list in enumerate(lists)]
            smallest = min(gather)
            final_data.append(smallest)
            smallest_index = gather.index(smallest)
            start_indices[smallest_index] += 1

            
            mask = []
            for index, start_index in enumerate(start_indices):
                if start_index == len(lists[index]._data_):
                    mask.append(0)
                else:
                    mask.append(1)

            start_indices = [st for i, st in enumerate(start_indices) if mask[i] == 1]
            lists = [ls for i, ls in enumerate(lists) if mask[i] == 1]


list1 = List([1, 10, 23, 100])
list2 = List([0, 2, 90])
list3 = List([-1, -2, 120])

print(list1.merge_sorted(list2))
print(list2.merge_sorted(list1))
print(Operations().merged_sort([list1, list2, list3]))