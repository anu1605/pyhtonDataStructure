from queue_list import Queue

queue_array = Queue(5)
queue_array.push(4)
queue_array.push(1)
queue_array.push(7)
queue_array.push(10)
queue_array.push(5)


queue_array.display()
queue_array.pop()
queue_array.push(120)
print("displaying queue")

queue_array.display()
