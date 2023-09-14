
from linkedLists import LinkedList

linkedList = LinkedList()

linkedList.insert(5)
linkedList.insert(6)
linkedList.insert(8)
linkedList.insert(12)
linkedList.print()
print("head points to", linkedList.get_head())
print("tail points to", linkedList.get_tail())
print(linkedList.total_nodes())
