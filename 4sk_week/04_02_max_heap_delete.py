class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        items = self.items

        if len(items) == 1:
            return

        items[1], items[-1] = items[-1], items[1]

        delete_node = items.pop()

        cur_index = 1
        length = len(items) - 1
        while cur_index <= length:
            left_index = cur_index * 2
            right_index = cur_index * 2 + 1

            if left_index > length:
                break

            max_index = left_index
            if right_index <= length:
                max_index = left_index if items[left_index] > items[right_index] else right_index

            if items[max_index] < items[cur_index]:
                break

            items[cur_index], items[max_index] = items[max_index], items[cur_index]
            cur_index = max_index

        return delete_node  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]