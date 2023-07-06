# A stack is used to add and remove data
# stack as in, "stack of books"
# If a book is added on top of an existing stack of books, the last one added, is first removed. 

stack = []
stack.append(1) 
stack.append(2) 
stack.append(3) 
stack.append(4) 

stack.pop(-1)

print(stack)

