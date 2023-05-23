class Queue:
    def __init__(self):
        self.items = []# Khởi tạo một hàng đợi rỗng

    def is_empty(self):# is_empty(): Kiểm tra xem hàng đợi có trống hay không.
        return len(self.items) == 0

    def enqueue(self, item):#enqueue(item): Thêm một phần tử vào cuối hàng đợi.
        self.items.append(item)

    def dequeue(self): #dequeue(): Xóa và trả về phần tử đầu tiên của hàng đợi
        if self.is_empty(): # Nếu hàng đợi rỗng, trả về thông báo "Queue is empty".
            return "Queue is empty"
        return self.items.pop(0)

    def size(self): #size(): Trả về số lượng phần tử hiện có trong hàng đợi.
        return len(self.items) 
    
    def print_items(self):
        print("Queue items:")
        for item in self.items:
            print(item)

"""Trong đoạn code trên, phương thức size() truy cập thuộc tính items của đối tượng hàng đợi 
và sử dụng hàm len() để đếm số phần tử trong danh sách items. 
Kết quả trả về là kích thước của hàng đợi, được tính bằng cách đếm số phần tử hiện có trong danh sách."""

    
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(10)

queue.print_items()

print("Queue size:", queue.size())  # Output: 3

print("Dequeued item:", queue.dequeue())  # Output: 1

print("Is queue empty?", queue.is_empty())  # Output: False


