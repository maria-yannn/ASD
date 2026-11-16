#сложность алгоритма: время - O(n); память - O(1)

data = [1, 2, 3, 4, 5]

# Definition for singly-linked list.
class ListNode: # ячейка односвязного списка (нода)
     def init(self, value=0, nextNode=None):
         self.val = value # через точку это типа поле (переменные, хранящиеся внутри класса)
         self.next = nextNode

class Solution: # мы не всегда используем конструктор классов, нам он не нужен в этом классе потому что он только для функц
    def reverseList(self, head: ListNode) -> ListNode: # 
        prev = None
        curr = head 

        while curr: # цикл до того момента пока curr не станет None
            nxt = curr.next
            curr.next = prev # разворот стрелочки обращаемся к значению next внутри curr
            prev = curr
            curr = nxt

        return prev
#Строит односвязный список из массива
def build_list(values):
    dummy = ListNode()          # фиктивный узел-заглушка перед головой
    tail = dummy
    for v in values:
        tail.next = ListNode(v) # прицепляем новый узел в конец
        tail = tail.next        # сдвигаем хвост
    return dummy.next           # настоящая голова

#превращает односвязный список в обычный массив
def to_pylist(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head = build_list(data)
print(to_pylist(head))                      # [1, 2, 3, 4, 5]

reversed_head = Solution().reverseList(head)
print(to_pylist(reversed_head))             # [5, 4, 3, 2, 1]