class Stack:
    def __init__(self): 
        self.items = []
#Đoạn mã trên định nghĩa một class Stack và khởi tạo một danh sách (list) trống items trong hàm khởi tạo __init__.

    def is_empty(self):
        return len(self.items) == 0
#Phương thức is_empty kiểm tra xem stack có rỗng hay không. Nó trả về True nếu stack rỗng và False nếu không.

    def push(self, item):
        self.items.append(item)
#Phương thức push thêm một phần tử vào đỉnh của stack. Nó sử dụng phương thức append của danh sách để thêm phần tử vào cuối danh sách items.

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    """Phương thức pop lấy phần tử ở đỉnh stack và loại bỏ nó khỏi stack. 
    Trước khi lấy phần tử, nó kiểm tra xem stack có rỗng hay không bằng cách gọi phương thức is_empty. 
    Nếu stack rỗng, nó sẽ ném một ngoại lệ (Exception) thông báo rằng stack đang rỗng. Nếu stack không rỗng, 
    nó sử dụng phương thức pop của danh sách để lấy và trả về phần tử ở đỉnh stack."""

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    """Phương thức peek trả về phần tử ở đỉnh stack mà không loại bỏ nó. Nó cũng kiểm tra xem stack có rỗng hay không trước khi truy cập đỉnh.
    Nếu stack rỗng, nó sẽ ném một ngoại lệ (Exception) tương tự như phương thức pop. 
    Nếu stack không rỗng, nó trả về phần tử ở vị trí cuối cùng của danh sách items (đỉnh stack)."""

    def size(self):
        return len(self.items)
#Phương thức size trả về kích thước (số lượng phần tử) của stack bằng cách sử dụng hàm len trên danh sách items.



stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  # Output: 3

print("Top item:", stack.peek())  # Output: 3

item = stack.pop()
print("Popped item:", item)  # Output: 3

print("Is stack empty?", stack.is_empty())  # Output: False
