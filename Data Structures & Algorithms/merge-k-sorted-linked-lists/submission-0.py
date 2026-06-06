# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class CustomMinHeap:

    def __init__(self):
        self.heap = []
        self.head = None
        self.prev = None

    def get_head(self):
        return self.head

    def push(self, list_head):
        while list_head:
            self.heap.append(list_head.val)
            self.heapify_up()
            list_head = list_head.next

    def pop_all(self):
        while self.heap:
            self.heapify_down()

    def get_parent_index(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx >= 0:
            return parent_idx
        return None

    def get_left_child(self, idx):
        left_child = (idx * 2) + 1
        if left_child < len(self.heap):
            return left_child
        return None
    
    def get_right_child(self, idx):
        right_child = (idx * 2) + 2
        if right_child < len(self.heap):
            return right_child
        return None

    def heapify_up(self):
        new_index = len(self.heap) - 1
        parent_index = self.get_parent_index(new_index)
        while parent_index is not None and self.heap[new_index] < self.heap[parent_index]:
            self.heap[new_index], self.heap[parent_index] = self.heap[parent_index], self.heap[new_index]
            new_index = parent_index
            parent_index = self.get_parent_index(new_index)

    def heapify_down(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = temp
        node = ListNode(self.heap.pop())
        if not self.head:
            self.head = node
        if self.prev:
            self.prev.next = node
        self.prev = node

        idx = 0
        left_child = self.get_left_child(idx)
        right_child = self.get_right_child(idx)
        smaller_child = None
        while left_child or right_child:
            if left_child and right_child:
                if self.heap[left_child] <= self.heap[right_child]:
                    smaller_child = left_child
                else:
                    smaller_child = right_child
            elif left_child:
                smaller_child = left_child
            elif right_child:
                smaller_child = right_child

            if self.heap[idx] > self.heap[smaller_child]:
                self.heap[idx], self.heap[smaller_child] = self.heap[smaller_child], self.heap[idx]
                idx = smaller_child
                left_child = self.get_left_child(idx)
                right_child = self.get_right_child(idx)
            else:
                break
            

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        custom_min_heap = CustomMinHeap()
        for linked_list in lists:
            custom_min_heap.push(linked_list)

        custom_min_heap.pop_all()
        return custom_min_heap.get_head()
        