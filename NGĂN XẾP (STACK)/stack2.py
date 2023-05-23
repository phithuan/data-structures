import numpy.random as rd
stack = rd.randint(0,100, size=(10))
#print(type(stack)) #<class 'numpy.ndarray'> nên phía dưới sẽ ép sang kiểu list

stack = list(stack) # đã ép kiểu list
print("tìm max của stack ?", stack)
m = stack.pop()

while stack:
    b = stack.pop()
    if b > m:
        print("do {} lớn hơn {} nên ta lấy {} ".format(b,m,b))
        m = b
    else:
        print("-do {} bé hơn {} nên ta giữ {}".format(b,m,m))
print("max:", m)





