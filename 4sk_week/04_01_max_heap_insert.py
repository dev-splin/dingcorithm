class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)

        cur_index = len(self.items) - 1
        items = self.items
        while cur_index != 1:
            parent_index = cur_index // 2

            if items[parent_index] <= value:
                items[parent_index], items[cur_index] = items[cur_index], items[parent_index]
                cur_index = parent_index
            else:
                break
        # 구현해보세요!
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!