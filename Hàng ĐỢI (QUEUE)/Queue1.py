class Node:
    def __init__(self, value):
        self.value = value #Thuộc tính value lưu trữ giá trị của nút.
        self.next = None#Thuộc tính next là một tham chiếu đến nút tiếp theo trong danh sách.

class Queue:
    def __init__(self):
        self.front = None  # Đỉnh hàng đợi
        self.rear = None  # Đuôi hàng đợi

    def is_empty(self):
        return self.front is None  # Kiểm tra xem hàng đợi có rỗng không  bằng cách kiểm tra xem front có trỏ đến None hay không.

    def enqueue(self, item): # được sử dụng để thêm một phần tử mới vào hàng đợi.
        new_node = Node(item) #Đầu tiên, một nút mới được tạo ra với giá trị là item bằng cách khởi tạo đối tượng Node với item là tham số.
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self): #lấy và loại bỏ phần tử đầu tiên khỏi hàng đợi
        if self.is_empty():
            raise Exception("Queue is empty")  # Nếu hàng đợi rỗng, ném ngoại lệ
        else:
            item = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")  # Nếu hàng đợi rỗng, ném ngoại lệ
        else:
            return self.front.value

    def size(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.next
        return count


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: 3

print("Front item:", queue.peek())  # Output: 1

item = queue.dequeue()
print("Dequeued item:", item)  # Output: 1

print("Is queue empty?", queue.is_empty())  # Output: False

print("ĐÉO HIỂU")